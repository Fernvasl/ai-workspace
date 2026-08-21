from ai_workspace.version import APP_NAME, STATUS, VERSION


def main() -> None:
    """Start AI Workspace."""
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print(f"Status: {STATUS}")


if __name__ == "__main__":
    main()