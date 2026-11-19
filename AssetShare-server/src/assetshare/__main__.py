import argparse

import uvicorn

from assetshare.app import app
from assetshare.core import info


def main() -> None:
    parser = argparse.ArgumentParser(description=info.DESCRIPTION)

    _ = parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind the server to (default: localhost)",
    )
    _ = parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port to bind the server to (default: 8080)",
    )
    _ = parser.add_argument(
        "--debug",
        type=bool,
        default=False,
        help="Enable debug mode (default: False)",
    )

    args = parser.parse_args()
    host: str = args.host  # pyright: ignore[reportAny]
    port: int = args.port  # pyright: ignore[reportAny]
    debug: bool = args.debug  # pyright: ignore[reportAny]

    if port < 1 or port > 65535:
        print(f"ERROR: Port must be between 1 and 65535, got {port}")
        return

    uvicorn.run(app, host=host, port=port, reload=debug)


if __name__ == "__main__":
    main()
