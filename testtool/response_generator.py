"""Generate mock API responses from OpenAPI schemas."""

import random
import string


class ResponseGenerationError(Exception):
    """Raised when response cannot be generated from schema."""


def generate_response(schema: dict) -> str | int | float | bool | dict:
    """
    Generate a mock response value from a schema.

    Args:
        schema: OpenAPI schema definition (must have 'type' field)

    Returns:
        Generated value matching the schema type

    Raises:
        ResponseGenerationError: If schema is invalid or type is unsupported
    """
    if "type" not in schema:
        raise ResponseGenerationError("Schema must define a 'type' field")

    schema_type = schema["type"]

    if schema_type == "string":
        return _generate_string()
    elif schema_type == "integer":
        return _generate_integer()
    elif schema_type == "number":
        return _generate_number()
    elif schema_type == "boolean":
        return _generate_boolean()
    elif schema_type == "object":
        return _generate_object(schema)
    else:
        raise ResponseGenerationError(f"Unsupported schema type: {schema_type}")


def _generate_string() -> str:
    """Generate a random string value."""
    length = random.randint(5, 15)
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def _generate_integer() -> int:
    """Generate a random integer value."""
    return random.randint(1, 1000)


def _generate_number() -> float:
    """Generate a random number (float) value."""
    return round(random.uniform(1.0, 1000.0), 2)


def _generate_boolean() -> bool:
    """Generate a random boolean value."""
    return random.choice([True, False])


def _generate_object(schema: dict) -> dict:
    """Generate a random object value from object schema."""
    if "properties" not in schema:
        raise ResponseGenerationError("Object schema must define 'properties' field")

    properties = schema["properties"]
    result = {}

    for prop_name, prop_schema in properties.items():
        result[prop_name] = generate_response(prop_schema)

    return result
