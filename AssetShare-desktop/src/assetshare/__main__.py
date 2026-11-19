import sys

from assetshare.app import run


def main() -> None:
    """Launch the AssetShare desktop application."""

    sys.exit(run(sys.argv))


if __name__ == "__main__":
    main()
