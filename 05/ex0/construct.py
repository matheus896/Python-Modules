import os
import site
import sys


def is_virtual_environment() -> bool:
    """Return True when the interpreter runs inside a virtual environment."""
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def site_packages_path() -> str:
    """Return the first site-packages directory of this interpreter."""
    paths = site.getsitepackages()
    return paths[0] if paths else "unknown"


def show_sealed_laboratory() -> None:
    """Describe an interpreter that runs inside a virtual environment."""
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")
    print()
    print("Reagent installation path:")
    print(site_packages_path())
    print()
    print("Global interpreter path:")
    print(sys.base_prefix)


def show_open_laboratory() -> None:
    """Describe an interpreter that runs in the global environment."""
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("Global package location:")
    print(site_packages_path())
    print()
    print("To seal the laboratory, run:")
    print("  python3 -m venv lab_env")
    print("  source lab_env/bin/activate        # On Unix")
    print("  lab_env\\Scripts\\activate           # On Windows")
    print("Then run this program again.")


def main() -> None:
    """Detect the current environment and explain how to isolate it."""
    if is_virtual_environment():
        show_sealed_laboratory()
    else:
        show_open_laboratory()


if __name__ == "__main__":
    main()
