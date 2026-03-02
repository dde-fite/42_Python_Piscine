from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class InvalidFormat(Exception):
    """Exception raised when incoming stream data does not match the expected\
          format."""
    pass


class DataStream(ABC):
    """Abstract base class for all data stream types."""
    def __init__(self, stream_id: str, stream_type: str, data_type: str):
        """Initializes the base stream metadata.

        Args:
            stream_id (str): Identifier of the stream.
            stream_type (str): Category of the stream.
            data_type (str): Description of the data carried by the stream.
        """
        self.__stream_id: str = stream_id
        self.__stream_type: str = stream_type
        self.__data_type: str = data_type
        self._processed_count: int = 0

    @property
    def stream_id(self):
        """Returns the ID of the stream."""
        return self.__stream_id

    @property
    def stream_type(self):
        """Returns the category of the stream."""
        return self.__stream_type

    @property
    def data_type(self):
        """Returns the description of the data carried by the stream."""
        return self.__data_type

    @property
    def processed_count(self):
        """Returns the number of processed data entries."""
        return self._processed_count

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes a batch of incoming data.

        Args:
            data_batch (List[Any]): Raw batch of streamed data.

        Returns:
            str: Human-readable description of the processing result.
        """
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filters incoming data based on a string prefix criterion.

        Args:
            data_batch (List[Any]): Batch of raw stream data.
            criteria (Optional[str]): Prefix used to filter data entries.

        Returns:
            List[Any]: Filtered list of matching data values.
        """
        if criteria is None:
            return data_batch
        l_return: list[str] = []
        for d in data_batch:
            try:
                if not isinstance(d, str):
                    raise InvalidFormat("Incorrect format!")
                parts = d.split(":", 1)
                if parts[0] == criteria:
                    if len(parts) > 1:
                        l_return.append(parts[1])
                    else:
                        l_return.append(parts[0])
            except InvalidFormat as e:
                print(e)
        return l_return

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns aggregated statistics of the stream.

        Returns:
            Dict[str, Union[str, int, float]]: Stream metadata and processing
            counters.
        """
        return {
            "stream_id": self.__stream_id,
            "stream_type": self.__stream_type,
            "processed_count": self._processed_count,
        }


class SensorStream(DataStream):
    """Data stream specialized for environmental sensor readings."""
    def __init__(self, stream_id: str):
        """Initializes a sensor data stream.

        Args:
            stream_id (str): Identifier of the sensor stream.
        """
        super().__init__(stream_id, "Sensor", "Environmental Data")
        self.__temps: list[float] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes a batch of sensor readings.

        Extracts temperature values and updates internal statistics.

        Args:
            data_batch (List[Any]): Batch of sensor data entries.

        Returns:
            str: Description of the processed batch.
        """
        temps = self.filter_data(data_batch, "temp")
        for t in temps:
            try:
                self.__temps.append(float(t))
            except ValueError:
                print("Invalid type")
        self._processed_count += len(data_batch)
        return f"Processing transaction batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns sensor-specific statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Stream statistics including
            average temperature.
        """
        return {
                    **super().get_stats(),
                    "avg_tmp": sum(self.__temps) / len(self.__temps)
                    if len(self.__temps) else 0
               }


class TransactionStream(DataStream):
    """Data stream specialized for financial transaction events."""
    def __init__(self, stream_id: str):
        """Initializes a transaction data stream.

        Args:
            stream_id (str): Unique identifier of the transaction stream.
        """
        super().__init__(stream_id, "Transation", "Financial Data")
        self.__ops: list[int] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes a batch of financial transactions.

        Parses buy and sell operations and computes net flow.

        Args:
            data_batch (List[Any]): Batch of transaction data.

        Returns:
            str: Description of the processed batch.
        """
        buy = self.filter_data(data_batch, "buy")
        sell = self.filter_data(data_batch, "sell")
        for b in buy:
            try:
                self.__ops.append(int(b))
            except ValueError:
                print("Invalid type")
        for s in sell:
            try:
                self.__ops.append(-int(s))
            except ValueError:
                print("Invalid type")
        self._processed_count += len(data_batch)
        return f"Processing transaction batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns transaction-specific statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Stream statistics including
            net transaction flow.
        """
        return {
                    **super().get_stats(),
                    "net": sum(self.__ops)
               }


class EventStream(DataStream):
    """Data stream specialized for system event monitoring."""
    def __init__(self, stream_id: str):
        """Initializes an event monitoring stream.

        Args:
            stream_id (str): Unique identifier of the event stream.
        """
        super().__init__(stream_id, "Event", "System Events")
        self.__errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes a batch of system events.

        Counts error-level events and updates processing statistics.

        Args:
            data_batch (List[Any]): Batch of system event entries.

        Returns:
            str: Description of the processed batch.
        """
        self.__errors += len(self.filter_data(data_batch, "error"))
        self._processed_count += len(data_batch)
        return f"Processing transaction batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns event-specific statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Stream statistics including
            detected error count.
        """
        return {
                    **super().get_stats(),
                    "errors": self.__errors
               }


class StreamProcessor:
    """Coordinator for managing and processing multiple data streams."""
    def __init__(self) -> None:
        """Initializes the stream processor."""
        self.__streams: List[DataStream] = []

    def stream(self, stream_id: str) -> DataStream:
        """Retrieves a registered stream by its identifier.

        Args:
            stream_id (str): Identifier of the desired stream.

        Returns:
            DataStream: Matching registered stream.

        Raises:
            KeyError: If the stream is not found.
        """
        for s in self.__streams:
            if s.stream_id == stream_id:
                return s
        raise KeyError("Stream not found")

    def register_stream(self, stream: DataStream):
        """Registers a new data stream.

        Args:
            stream (DataStream): Stream instance to be registered.
        """
        self.__streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]):
        """Processes batches for all registered streams.

        Args:
            batches (Dict[str, List[Any]]): Mapping of stream IDs to data
            batches.

        Returns:
            List[Dict[str, Union[str, int, float]]]: Aggregated statistics
            from all processed streams.
        """
        results: list[Dict[str, Union[str, int, float]]] = []
        for s_id, batch in batches.items():
            try:
                stream = self.stream(s_id)
                stream.process_batch(batch)
                results.append(stream.get_stats())
            except KeyError as e:
                print(e)
        return results


print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

sensor = SensorStream("SENSOR_001")
transaction = TransactionStream("TRANS_001")
event = EventStream("EVENT_001")

print("\nInitializing Sensor Stream...\n"
      f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}\n"
      f"{sensor.process_batch(['temp:22.5', 'humidity:65', 'pressure:1013'])}")
stats = sensor.get_stats()
print(f"Sensor analysis: {stats['processed_count']} readings processed, "
      f"avg temp: {stats['avg_tmp']}ºC")

print("\nInitializing Transaction Stream...\n"
      f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}\n"
      f"{transaction.process_batch(['buy:100', 'sell:150', 'buy:75'])}")
stats = transaction.get_stats()
print(f"Transaction analysis: {stats['processed_count']} operations, "
      f"net flow: {['', '+'][int(stats['net']) > 0] + str(stats['net'])} "
      "units")

print("\nInitializing Event Stream...\n"
      f"Stream ID: {event.stream_id}, Type: {event.stream_type}\n"
      f"{event.process_batch(['login', 'error', 'logout'])}")
stats = event.get_stats()
print(f"Event analysis: {stats['processed_count']} events, {stats['errors']} "
      f"error{'s' if int(stats['errors']) > 1 else ''} detected")

print("\n=== Polymorphic Stream Processing ===\n"
      "Processing mixed stream types through unified interface...")
processor = StreamProcessor()
processor.register_stream(SensorStream("SENSOR_001"))
processor.register_stream(TransactionStream("TRANS_001"))
processor.register_stream(EventStream("EVENT_001"))

mixed_batches = {
    "SENSOR_001": ["temp:30.0", "temp:28.0"],
    "TRANS_001": ["buy:200", "sell:50", "buy:100", "sell:75"],
    "EVENT_001": ["login", "error", "error"],
}

results = processor.process_all(mixed_batches)
print(f"Batch {len(results)} Results:")
for res in results:
    print(f"- {res['stream_type']} data: {res['processed_count']} proccesed")

print("\nStream filtering active: High-priority data only")
filtered = sensor.filter_data(
    ["temp:100", "temp:22", "alert:critical"], "critical"
)
print("Filtered results:",
      len(sensor.filter_data(
          ['critical:temp', 'critical:wind', 'pressure:1000'],
          'critical')
          ),
      "critical sensor alerts,",
      len(transaction.filter_data(
          ['buy:10000', 'sell:23'],
          'buy')
          ),
      "large transaction")

print("\nAll streams processed successfully. Nexus throughput optimal.")
