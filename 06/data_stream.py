"""Polymorphic stream processing on top of the data processors."""

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
        return "Data Processor"

    @property
    def total_processed(self) -> int:
        return self._total

    @property
    def pending(self) -> int:
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


class DataStream:
    """Route each stream element to the first processor that accepts it."""

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        print("Initialize Data Stream...")

    def register_processor(self, proc: DataProcessor) -> None:
        """Add a processor to the stream."""
        self.processors.append(proc)
        print(f"Registering {proc.label}")

    def process_stream(self, stream: list[Any]) -> None:
        """Send every element to a compatible processor."""
        for element in stream:
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print("DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        """Print how much data each processor has seen and still holds."""
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for processor in self.processors:
            print(
                f"{processor.label}: total {processor.total_processed} items "
                f"processed, remaining {processor.pending} on processor"
            )


def main() -> None:
    """Demonstrate a stream with one and then three processors."""
    print("=== Code Nexus - Data Stream ===")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
