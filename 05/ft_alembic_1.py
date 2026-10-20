import alchemy


def main() -> None:
    """Use the package interface and show what it does not expose."""
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print()
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:")
    try:
        print(alchemy.create_earth())
    except AttributeError as error:
        print(f"AttributeError: {error}")


if __name__ == "__main__":
    main()
