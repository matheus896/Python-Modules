import sys
import typing


def read_file(filename: str) -> str:
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


def transform_data(content: str) -> str:
    """Append the archive character to the end of each line

    Args:
        content: The original content of the file.

    Returns:
        The content with '#' appended to every line.
    """
    lines: list[str] = content.splitlines()
    return "\n".join(line + "#" for line in lines)


def save_file(filename: str, content: str) -> None:
    """Write content to a file, creating or replacing it.

    Args:
        filename: The name of the file to write to.
        content: The content to save.
    """
    file: typing.IO[str] = open(filename, "w")
    file.write(content)
    file.close()


def main() -> None:
    """Read, transform and save thew content of a file."""
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        content: str = read_file(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---\n")
    print(content)
    print("\n---")
    print(f"File '{filename}' closed.")

    transformed: str = transform_data(content)
    print("Transform data:")
    print("---\n")
    print(transformed)
    print("\n---")

    save_name: str = input("Enter new file name (or empty): ")
    if not save_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{save_name}'")
    try:
        save_file(save_name, transformed)
    except OSError as e:
        print(f"Error opening file '{save_name}': {e}")
        print("Data not saved.")
    else:
        print(f"Data saved in file '{save_name}'.")


if __name__ == "__main__":
    main()
