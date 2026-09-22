"""CLI entry point for the OpenAPI mock server."""

import argparse
import sys

from testtool.server import create_app
from testtool.spec_loader import SpecLoadError, load_spec


def main() -> None:
    """Parse arguments and start the mock server."""
    parser = argparse.ArgumentParser(
        description='OpenAPI Mock Server - Generate mock API responses from specifications'
    )
    parser.add_argument(
        '--spec',
        required=True,
        help='Path to OpenAPI specification file (YAML or JSON)',
    )
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to listen on (default: 5000)',
    )

    args = parser.parse_args()

    try:
        spec = load_spec(args.spec)
    except SpecLoadError as e:
        print(f"Error loading specification: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        app = create_app(spec)
        app.run(host='0.0.0.0', port=args.port, debug=False)
    except OSError as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
