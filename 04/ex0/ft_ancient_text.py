import sys
import typing


def get_file_content(filename: str) -> str:
    """Read the full content of a file.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file.
    """
    file: typing.IO[str] = open(filename, "r")
    content: str = file.read()
    file.close()
    return content


def main() -> None:
    """Recover and display the content of a file."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        content: str = get_file_content(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---\n")
    print(content)
    print("\n---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
