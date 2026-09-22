import pytest

from testtool.response_generator import ResponseGenerationError, generate_response


class TestGenerateStringResponse:
    def test_generate_string_value_from_schema(self):
        """Generate string value from schema with type 'string'"""
        schema = {"type": "string"}
        response = generate_response(schema)
        assert isinstance(response, str)
        assert len(response) > 0


class TestGenerateIntegerResponse:
    def test_generate_integer_value_from_schema(self):
        """Generate integer value from schema with type 'integer'"""
        schema = {"type": "integer"}
        response = generate_response(schema)
        assert isinstance(response, int)


class TestGenerateNumberResponse:
    def test_generate_number_value_from_schema(self):
        """Generate number value from schema with type 'number'"""
        schema = {"type": "number"}
        response = generate_response(schema)
        assert isinstance(response, (int, float))


class TestGenerateBooleanResponse:
    def test_generate_boolean_value_from_schema(self):
        """Generate boolean value from schema with type 'boolean'"""
        schema = {"type": "boolean"}
        response = generate_response(schema)
        assert isinstance(response, bool)


class TestRejectInvalidSchema:
    def test_reject_schema_missing_type(self):
        """Reject invalid schema with missing type field"""
        schema = {"properties": {}}
        with pytest.raises(ResponseGenerationError):
            generate_response(schema)


class TestRejectUnsupportedType:
    def test_reject_unknown_schema_type(self):
        """Handle unknown schema type gracefully"""
        schema = {"type": "unsupported_type"}
        with pytest.raises(ResponseGenerationError):
            generate_response(schema)
