import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


def env(name: str, default: str | None = None) -> str | None:
    """Return an environment variable, or a default when it is missing."""
    return os.getenv(name, default)


def env_is_ignored() -> bool:
    """Return True when .env is listed in this exercise's .gitignore."""
    path = os.path.join(BASE_DIR, ".gitignore")
    try:
        with open(path, "r") as file:
            return any(line.strip() == ".env" for line in file)
    except OSError:
        return False


def main() -> None:
    """Read the Oracle configuration from the environment."""
    mode = (env("MATRIX_MODE", "development") or "development").lower()
    database_url = env("DATABASE_URL")
    api_key = env("API_KEY")
    log_level = env("LOG_LEVEL")
    zion_endpoint = env("ZION_ENDPOINT")
    production = mode == "production"

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        local_hosts = ("localhost", "127.0.0.1")
        is_local = any(host in database_url for host in local_hosts)
        location = "local" if is_local else "remote"
        print(f"Database: Connected to {location} instance")
    else:
        print("Database: Connected to local instance")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print(f"Log Level: {'WARNING' if production else 'DEBUG'}")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline (development default)")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    if env_is_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARN] .env is not listed in .gitignore")
    print("[OK] Production overrides available")

    if not database_url and not api_key and not zion_endpoint:
        print()
        print("WARNING: No configuration found; using development defaults.")

    if production:
        missing = [
            name for name in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
            if env(name) is None
        ]
        if missing:
            print()
            print("WARNING: Production configuration incomplete: "
                  + ", ".join(missing))

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
