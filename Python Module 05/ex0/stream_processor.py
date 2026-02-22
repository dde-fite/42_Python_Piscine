from typing import Any
from abc import ABC, abstractmethod


class InvalidData(Exception):
    """Exception for errors with data in processors."""
    pass


class DataProcessor(ABC):
    """Common pipeline between processors for interacting with them.

    This interface is composed of the following definitions: process,\
        validate, and format_output.

    Implementations are defined by the children except for format_output that\
        follows a concrete implementation.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """Treatment of data using the processor's rules.

        Args:
            data (Any): Data to be proccesed

        Returns:
            str: Processed data.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Checks that data follows the processor's format.

        Args:
            data (Any): Data to be analyzed

        Returns:
            bool: Returns True if it is in an accepted format, False otherwise.
        """
        pass

    def format_output(self, result: str) -> str:
        """Returns the data as a ready-to-print string.

        Args:
            result (str): Processed data

        Returns:
            str: String ready to be printed.
        """
        return "Output: " + result


class NumericProcessor(DataProcessor):
    """Implementation the DataProcessor class for processing numbers."""
    def process(self, data: Any) -> str:
        """Parses and analyzes the submitted data in the format of a list, str\
            or single number, then returns its stats in a string.

        Args:
            data (Any): Data to be proccesed. int, float, list[int | float],\
                str.

        Returns:
            str: Stats of the processed data.
        """
        nums: list[int | float] = []
        if isinstance(data, list):
            for n in data:
                if isinstance(n, int | float):
                    nums.append(n)
                else:
                    return ""
        elif isinstance(data, str):
            data = data.split(',')
            for n in data:
                try:
                    nums.append(int(n))
                except ValueError:
                    return ""
        elif isinstance(data, int | float):
            nums.append(data)
        nums_len = len(nums)
        nums_sum = sum(nums)
        return (f"Processed {nums_len} numeric values, sum={nums_sum}, "
                f"avg={nums_sum / nums_len}")

    def validate(self, data: Any) -> bool:
        """Validates that the processed numeric data follows the expected\
            format.

        Args:
            data (Any): Data to be validated.

        Returns:
            bool: True if the data matches the expected processed numeric\
                format, False otherwise.
        """
        try:
            if not isinstance(data, str):
                raise InvalidData("Data was expected to be an str")

            parts = data.split()
            if not (
                len(parts) == 6
                and parts[0] == "Processed"
                and parts[1].isdigit()
                and parts[2] == "numeric"
                and parts[3] == "values,"
            ):
                raise InvalidData("Data format is incorrect")
        except InvalidData as e:
            print(f"Validation: {e}")
            return False
        print("Validation: Numeric data verified")
        return True


class TextProcessor(DataProcessor):
    """Implementation of DataProcessor for processing plain text strings.

    This processor analyzes textual data and returns basic statistics such\
        as character and word count.
    """
    def process(self, data: Any) -> str:
        """Analyzes a text string and returns its basic statistics.

        Args:
            data (Any): Data to be processed. Expected to be a string.

        Returns:
            str: A string describing the number of characters and words,\
                or an empty string if the input is invalid.
        """
        if not isinstance(data, str):
            return ""
        chars = len(data)
        words = len(data.split(' '))
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        """Validates that the processed text follows the expected format.

        Args:
            data (Any): Data to be validated.

        Returns:
            bool: True if the data matches the expected processed text\
                format, False otherwise.
        """
        try:
            if not isinstance(data, str):
                raise InvalidData("Data was expected to be an str")

            parts = data.split()
            if not (
                len(parts) == 6
                and parts[0] == "Processed"
                and parts[1] == "text:"
                and parts[2].isdigit()
                and parts[3] == "characters,"
                and parts[4].isdigit()
                and parts[5] == "words"
            ):
                raise InvalidData("Data format is incorrect")
        except InvalidData as e:
            print(f"Validation: {e}")
            return False
        print("Validation: Text data verified")
        return True


class LogProcessor(DataProcessor):
    """Implementation of DataProcessor for processing log entries.

    This processor parses log messages, normalizes their severity level,\
        and formats them into a standardized alert-style output.
    """
    def process(self, data: Any) -> str:
        """Parses a log entry and formats it with a normalized severity level.

        Args:
            data (Any): Data to be processed. Expected to be a log string\
                starting with a log level (e.g., ERROR:, INFO:).

        Returns:
            str: A formatted log message, or an empty string if the input\
                is invalid.
        """
        if not isinstance(data, str):
            return ""
        parts = data.split(' ')
        raw_type = parts[0].removesuffix(':').upper()
        err_type: str = ""
        if raw_type == "ERROR":
            err_type = "ALERT"
        else:
            err_type = f"{raw_type}"
        return (f"[{err_type}] {raw_type} level detected: "
                f"{' '.join(parts[1:])}")

    def validate(self, data: Any) -> bool:
        """Validates that the processed log entry follows the expected format.

        Args:
            data (Any): Data to be validated.

        Returns:
            bool: True if the data matches the expected processed log
            format, False otherwise.
        """
        try:
            if not isinstance(data, str):
                raise InvalidData("Data was expected to be an str")

            parts = data.split()
            if not (
                len(parts) > 4
                and parts[0][0] == "["
                and parts[0][max(len(parts[0]) - 1, 0)] == "]"
                and parts[2] == "level"
                and parts[3] == "detected:"
            ):
                raise InvalidData("Data format is incorrect")
        except InvalidData as e:
            print(f"Validation: {e}")
            return False
        print("Validation: Log entry verified")
        return True


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
proccesors: list[DataProcessor] = [
    NumericProcessor(),
    TextProcessor(),
    LogProcessor()
    ]

print("\nInitializing Numeric Processor...\n"
      "Processing data: [1, 2, 3, 4, 5]")
data = proccesors[0].process([1, 2, 3, 4, 5])
proccesors[0].validate(data)
print(proccesors[0].format_output(data))

print("\nInitializing Text Processor...\n"
      'Processing data: "Hello Nexus World"')
data = proccesors[1].process("Hello Nexus World")
proccesors[1].validate(data)
print(proccesors[1].format_output(data))

print("\nInitializing Log Processor...\n"
      'Processing data: "ERROR: Connection timeout"')
data = proccesors[2].process("ERROR: Connection timeout")
proccesors[2].validate(data)
print(proccesors[2].format_output(data))

print("\n=== Polymorphic Processing Demo ==="
      "\nProcessing multiple data types through same interface...")
data_lst: list[Any] = [
    [0, 4, 2],
    "Hello World!",
    "INFO: System ready"]
i: int = 0
for p in proccesors:
    print(f"Result {i + 1}: {p.process(data_lst[i])}")
    i += 1

print("\nFoundation systems online. Nexus ready for advanced streams.")
