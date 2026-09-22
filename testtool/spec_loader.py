"""Load and parse OpenAPI/Swagger specifications."""

import json
from pathlib import Path

import yaml


class SpecLoadError(Exception):
    """Raised when spec file cannot be loaded or parsed."""


def load_spec(file_path: str) -> dict:
    """
    Load and parse an OpenAPI specification from YAML or JSON.

    Args:
        file_path: Path to the spec file (.yaml, .yml, or .json)

    Returns:
        Parsed specification as a dictionary

    Raises:
        SpecLoadError: If file not found, format is invalid, or parsing fails
    """
    path = Path(file_path)

    if not path.exists():
        raise SpecLoadError(f"Specification file not found: {file_path}")

    try:
        content = path.read_text()
    except OSError as e:
        raise SpecLoadError(f"Failed to read specification file: {e}")

    suffix = path.suffix.lower()

    try:
        if suffix in ('.yaml', '.yml'):
            spec = yaml.safe_load(content)
        elif suffix == '.json':
            spec = json.loads(content)
        else:
            raise SpecLoadError(f"Unsupported file format: {suffix}. Use .yaml, .yml, or .json")
    except yaml.YAMLError as e:
        raise SpecLoadError(f"Invalid YAML format: {e}")
    except json.JSONDecodeError as e:
        raise SpecLoadError(f"Invalid JSON format: {e}")

    if spec is None:
        raise SpecLoadError("Specification file is empty")

    return spec
