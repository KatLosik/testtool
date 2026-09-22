import pytest

from testtool.response_generator import ResponseGenerationError, generate_response


class TestGenerateArrayOfStrings:
    def test_generate_array_of_strings_with_multiple_elements(self):
        """Generate array of strings with multiple elements"""
        schema = {
            "type": "array",
            "items": {"type": "string"},
        }
        response = generate_response(schema)
        assert isinstance(response, list)
        assert len(response) == 3
        assert all(isinstance(item, str) for item in response)


class TestGenerateArrayOfIntegers:
    def test_generate_array_of_integers_with_multiple_elements(self):
        """Generate array of integers with multiple elements"""
        schema = {
            "type": "array",
            "items": {"type": "integer"},
        }
        response = generate_response(schema)
        assert isinstance(response, list)
        assert len(response) == 3
        assert all(isinstance(item, int) for item in response)


class TestGenerateArrayOfBooleans:
    def test_generate_array_of_booleans_with_multiple_elements(self):
        """Generate array of booleans with multiple elements"""
        schema = {
            "type": "array",
            "items": {"type": "boolean"},
        }
        response = generate_response(schema)
        assert isinstance(response, list)
        assert len(response) == 3
        assert all(isinstance(item, bool) for item in response)


class TestRejectArraySchemaMissingItems:
    def test_reject_array_schema_missing_items_field(self):
        """Reject array schema missing items field"""
        schema = {"type": "array"}
        with pytest.raises(ResponseGenerationError):
            generate_response(schema)
