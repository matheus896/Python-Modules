"""A complete pipeline: polymorphic input and duck-typed output plugins."""

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    """Duck-typed contract for output plugins."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Export one batch of processed values."""


class CSVExportPlugin:
    """Write values as one CSV line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    """Write values as a JSON object keyed by ingestion rank."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = [
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        ]
        print("{" + ", ".join(pairs) + "}")

    @staticmethod
    def _escape(value: str) -> str:
        return (
            value.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", "\\n")
        )


class DataStream:
    """Route stream input to processors and output to a plugin."""

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume up to nb values per processor and export each batch."""
        for processor in self.processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.pending == 0:
                    break
                batch.append(processor.output())
            if batch:
                plugin.process_output(batch)

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
    """Run two batches through both export plugins."""
    print("=== Code Nexus - Data Pipeline ===")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

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

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
