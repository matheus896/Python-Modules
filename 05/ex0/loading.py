import importlib


def check_reagent(name: str, description: str) -> bool:
    """Report whether one external reagent can be imported."""
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - {description} unavailable")
        return False

    version = getattr(module, "__version__", "unknown")
    print(f"[OK] {name} ({version}) - {description} ready")
    return True


def main() -> None:
    """Check the declared reagents and explain the two managers."""
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    pandas_ready = check_reagent("pandas", "Data manipulation")
    numpy_ready = check_reagent("numpy", "Numerical computation")

    print()
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it "
          "at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins "
          "the resolved")
    print("versions in poetry.lock so every install is identical.")
    print()

    if pandas_ready and numpy_ready:
        print("All reagents present and accounted for.")
        return

    print("Some reagents are missing. Install them with either tool:")
    print("  pip install -r ex0/requirements.txt")
    print("  poetry install")


if __name__ == "__main__":
    main()
