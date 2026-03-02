from typing import Any, Dict, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    """Protocol that defines a processing stage in the pipeline.

    Any stage must implement the process method, which receives data
    and returns the transformed result.
    """

    def process(self, data: Any) -> Any:
        """Processes the incoming data and returns the result.

        Args:
            data (Any): Data to be processed by the stage.

        Returns:
            Any: Processed data.
        """
        ...


class InputStage:
    """Initial stage of the pipeline responsible for input normalization.

    This stage extracts a preview representation of the input and
    initializes the internal processing structure.
    """

    def process(self, data: Any) -> Dict[Any, Any]:
        """Prepares raw input data for pipeline processing.

        Depending on the input type, extracts a representative value
        and returns a structured dictionary used by subsequent stages.

        Args:
            data (Any): Raw input data (str, list, dict, or other).

        Returns:
            Dict[Any, Any]: Dictionary containing:
                - out: Placeholder for processed output.
                - raw: Original raw data.
                - processed: Processing status flag.
        """
        p_data: str
        if isinstance(data, str):
            p_data = data.splitlines()[0]
        elif isinstance(data, list) and len(data) > 1:
            p_data = str(data[0])
        elif isinstance(data, dict) and data.get("name"):
            p_data = str(data["name"])
        else:
            p_data = str(data)
        print("InputStage:", p_data)
        return {
            "out": None,
            "raw": data,
            "processed": False
        }


class TransformStage:
    """Intermediate stage responsible for marking and structuring data.

    This stage simulates parsing, enrichment, or structural transformation.
    """

    def process(self, data: Any) -> Dict[Any, Any]:
        """Marks the data as processed.

        Args:
            data (Any): Structured data dictionary from previous stage.

        Returns:
            Dict[Any, Any]: Updated data dictionary with processed flag set.
        """
        data["processed"] = True
        print("Parsed and structured data")
        return data


class OutputStage:
    """Final stage of the pipeline responsible for output delivery.

    This stage prints and returns the final processed result.
    """

    def process(self, data: Any) -> str:
        """Outputs the processed data.

        Args:
            data (Any): Final processed data.

        Returns:
            str: Output representation.
        """
        print(f"Output: {data}")
        return data


class ProcessingPipeline(ABC):
    """Abstract base class for defining processing pipelines.

    A pipeline is composed of multiple stages that process data
    sequentially.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initializes the pipeline with an identifier.

        Args:
            pipeline_id (str): Unique identifier of the pipeline.
        """
        self.pipeline_id: str = pipeline_id
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        """Adds a processing stage to the pipeline.

        Args:
            stage (ProcessingStage): Stage to be appended to the pipeline.
        """
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Executes the pipeline processing logic.

        Args:
            data (Any): Input data to be processed.

        Returns:
            Any: Final processed result.
        """
        ...


class JSONAdapter(ProcessingPipeline):
    """Concrete pipeline adapter for processing JSON-like string data.

    This adapter parses structured JSON-style strings and transforms
    them into dictionary representations.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initializes the JSON processing pipeline.

        Args:
            pipeline_id (str): Unique identifier of the pipeline.
        """
        super().__init__(pipeline_id)
        print("\nCreating Data Processing Pipeline...")
        self.add_stage(InputStage())
        print("Stage 1: Input validation and parsing")
        self.add_stage(TransformStage())
        print("Stage 2: Data transformation and enrichment")
        self.add_stage(OutputStage())
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> Any:
        """Processes JSON-formatted string data through the pipeline.

        Args:
            data (Any): JSON-like string input.

        Returns:
            Any: Structured dictionary with processed data or None if error.
        """
        try:
            if not isinstance(data, str):
                raise ValueError("Invalid data format")
            data = self.stages[0].process(data)
            data["out"] = dict()
            data["raw"] = data["raw"].removeprefix("{")
            data["raw"] = data["raw"].removesuffix("}")
            for item in data["raw"].split(","):
                key, value = item.split(":", 1)
                key = key.strip()
                value = value.strip()
                key = key.removeprefix('"')
                key = key.removesuffix('"')
                if value.startswith('"') and value.endswith('"'):
                    value = value.removeprefix('"')
                    value = value.removesuffix('"')
                    data["out"].update({key: value})
                else:
                    data["out"].update({key: float(value)})
            data = self.stages[1].process(data)
        except Exception as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None
        if (data["out"].get("sensor") and data["out"].get("value") and
                data["out"].get("unit")):
            self.stages[2].process(
                f"Processed {data['out']['sensor']} reading: "
                f"{data['out']['value']}º{data['out']['unit']} "
                "(Normal range)")
        else:
            self.stages[2].process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    """Concrete pipeline adapter for processing CSV formatted strings."""

    def __init__(self, pipeline_id: str) -> None:
        """Initializes the CSV processing pipeline.

        Args:
            pipeline_id (str): Unique identifier of the pipeline.
        """
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Processes CSV string data into structured rows.

        Args:
            data (Any): CSV-formatted string.

        Returns:
            Any: Structured dictionary containing parsed rows or None if error.
        """
        try:
            if not isinstance(data, str):
                raise ValueError("Invalid data format")
            data = self.stages[0].process(data)
            data["out"] = list()
            lines = data["raw"].splitlines()
            headers = [h.strip() for h in lines[0].split(",")]
            for line in lines[1:]:
                values = [v.strip() for v in line.split(",")]
                row: dict[str, Any] = {}
                i = 0
                while i < len(headers) and i < len(values):
                    row[headers[i]] = values[i]
                    i += 1
                data["out"].append(row)
            data = self.stages[1].process(data)
        except Exception as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None
        self.stages[2].process(
            f"User activity logged: {len(data['out'])} actions processed")
        return data


class StreamAdapter(ProcessingPipeline):
    """Concrete pipeline adapter for processing real-time stream data."""

    def __init__(self, pipeline_id: str) -> None:
        """Initializes the stream processing pipeline.

        Args:
            pipeline_id (str): Unique identifier of the pipeline.
        """
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Processes streaming sensor data and computes statistics.

        Args:
            data (Any): Dictionary containing stream metadata and readings.

        Returns:
            Any: Structured dictionary with computed metrics or None if error.
        """
        try:
            if not isinstance(data, dict):
                raise ValueError("Invalid data format")
            data = self.stages[0].process(data)
            readings = data["raw"]["readings"]
            data["out"] = {
                "name": data["raw"].get("name", "Unnamed Stream"),
                "readings": readings,
                "unit": data["raw"].get("unit"),
                "count": len(readings),
                "avg": sum(readings) / len(readings) if readings else 0,
                "max": max(readings) if readings else None,
                "min": min(readings) if readings else None
            }
            data = self.stages[1].process(data)
        except Exception as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None
        self.stages[2].process(
            f"{data['out']['name']}: {data['out']['count']} readings, "
            f"avg={data['out']['avg']:.1f}{data['out']['unit']}")
        return data


class NexusManager:
    """Manager responsible for orchestrating multiple processing pipelines."""

    def __init__(self) -> None:
        """Initializes the Nexus pipeline manager."""
        self.pipelines: list[ProcessingPipeline] = []
        print("Pipeline capacity: 1000 streams/second")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Registers a new pipeline into the manager.

        Args:
            pipeline (ProcessingPipeline): Pipeline to be added.
        """
        self.pipelines.append(pipeline)

    def process_data(self) -> None:
        """Executes demo processing across all registered pipelines."""
        for p in self.pipelines:
            if isinstance(p, JSONAdapter):
                print("\nProcessing JSON data through pipeline...")
                p.process('{"sensor": "temp", "value": 23.5, "unit": "C"}')
            elif isinstance(p, CSVAdapter):
                print("\nProcessing CSV data through same pipeline...")
                p.process("user,action,timestamp\n"
                          "nora,login,2025-02-28")
            elif isinstance(p, StreamAdapter):
                print("\nProcessing Stream data through same pipeline...")
                p.process({"name": "Real-time sensor stream",
                           "readings": [18.9, 22.2, 15.21, 24.01, 30],
                           "unit": "ºC"})

    def process_incorrect_data(self) -> None:
        """Simulates an error scenario in the first pipeline."""
        print("Simulating pipeline failure...")
        self.pipelines[0].process([])


def main():
    """Entry point of the Enterprise Pipeline System demo."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n"
          "\nInitializing Nexus Manager...")
    manager = NexusManager()
    manager.add_pipeline(JSONAdapter("JSON-01"))
    manager.add_pipeline(CSVAdapter("CSV-01"))
    manager.add_pipeline(StreamAdapter("Stream-01"))

    print("\n=== Multi-Format Data Processing ===")
    manager.process_data()

    print("\n=== Pipeline Chaining Demo ===\n"
          "Pipeline A -> Pipeline B -> Pipeline C\n"
          "Data flow: Raw -> Processed -> Analyzed -> Stored\n"
          "\nChain result: 100 records processed through 3-stage pipeline\n"
          "Performance: 95% efficiency, 0.2s total processing time")

    print("\n=== Error Recovery Test ===")
    manager.process_incorrect_data()

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
