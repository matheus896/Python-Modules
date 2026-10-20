"""Data processors built on an abstract base class."""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Common interface for every data processor."""

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank = 0
        self._total = 0

    @property
    def label(self) -> str:
        """Human-readable processor name."""
        return "Data Processor"

    @property
    def total_processed(self) -> int:
        """Number of items ingested since this processor was created."""
        return self._total

    @property
    def pending(self) -> int:
        """Number of items still waiting to be extracted."""
        return len(self._data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True when this processor can ingest the data."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Store the data inside this processor."""

    def output(self) -> tuple[int, str]:
        """Extract the oldest value and its ingestion rank."""
        if not self._data:
            raise IndexError("No data available")
        return self._data.pop(0)

    def _store(self, value: str) -> None:
        self._data.append((self._next_rank, value))
        self._next_rank += 1
        self._total += 1


class NumericProcessor(DataProcessor):
    """Process integers, floats and lists of both."""

    @property
    def label(self) -> str:
        return "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(  # type: ignore[override]
        self, data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    """Process strings and lists of strings."""

    @property
    def label(self) -> str:
        return "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: str | list[str]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    """Process dictionaries of string key-value pairs."""

    @property
    def label(self) -> str:
        return "Log Processor"

    @staticmethod
    def _is_log(data: Any) -> bool:
        return (
            isinstance(data, dict)
            and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        )

    def validate(self, data: Any) -> bool:
        if self._is_log(data):
            return True
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item.get("log_level", "LOG")
            message = item.get("log_message", str(item))
            self._store(f"{level}: {message}")


def main() -> None:
    """Demonstrate validation, ingestion and extraction."""
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except ValueError as error:
        print(f"Got exception: {error}")

    print()
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print()
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print()
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print()
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print()
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    print()
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
