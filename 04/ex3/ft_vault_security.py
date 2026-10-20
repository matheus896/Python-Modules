def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    """Safely read from or write to a file using a context manager.

    Args:
        filename: The name of the file to access.
        action: "read" or "write".
        content: The content to write when action is "write".

    Returns:
        A tuple with the success flag and the file content or an error
        message.
    """
    try:
        if action == "read":
            with open(filename, "r") as file:
                return True, file.read()
        if action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        return False, f"Unknown action: {action}"
    except OSError as error:
        return False, str(error)


def main() -> None:
    """Demonstrate secure reads and writes."""
    directory = __file__.rpartition("/")[0] or "."
    source: str = directory + "/../ex0/ancient_fragment.txt"
    destination: str = "/tmp/vault_security_archive.txt"

    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("Using 'secure_archive' to read from a regular file:")
    success, content = secure_archive(source)
    print((success, content))

    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive(destination, "write", content))
    else:
        print((False, content))


if __name__ == "__main__":
    main()
