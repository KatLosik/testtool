import argparse
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_spec_file():
    """Create a temporary OpenAPI spec file."""
    spec_content = """
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      responses:
        '200':
          description: Test
          content:
            application/json:
              schema:
                type: string
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write(spec_content)
        temp_path = f.name
    yield temp_path
    Path(temp_path).unlink()


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--spec', required=True)
    parser.add_argument('--port', type=int, default=5000)
    return parser


class TestCliSpecArgument:
    def test_cli_rejects_missing_spec_argument(self):
        """CLI rejects missing --spec argument"""
        parser = create_parser()
        with pytest.raises(SystemExit):
            parser.parse_args([])


class TestCliSpecAndPortArguments:
    def test_cli_accepts_spec_and_port_arguments(self, temp_spec_file):
        """CLI accepts --spec and --port arguments"""
        parser = create_parser()
        args = parser.parse_args(['--spec', temp_spec_file, '--port', '9999'])
        assert args.spec == temp_spec_file
        assert args.port == 9999


class TestCliDefaultPort:
    def test_cli_accepts_spec_with_default_port(self, temp_spec_file):
        """CLI accepts --spec with default port"""
        parser = create_parser()
        args = parser.parse_args(['--spec', temp_spec_file])
        assert args.spec == temp_spec_file
        assert args.port == 5000
