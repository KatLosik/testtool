import pytest

from testtool.response_generator import ResponseGenerationError, generate_response


class TestGenerateObjectWithPrimitiveProperties:
    def test_generate_object_with_string_and_integer_properties(self):
        """Generate object with string and integer properties"""
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
        }
        response = generate_response(schema)
        assert isinstance(response, dict)
        assert "name" in response
        assert "age" in response
        assert isinstance(response["name"], str)
        assert isinstance(response["age"], int)


class TestGenerateObjectWithMixedPrimitiveTypes:
    def test_generate_object_with_mixed_primitive_types(self):
        """Generate object with mixed primitive types"""
        schema = {
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "count": {"type": "integer"},
                "rating": {"type": "number"},
                "active": {"type": "boolean"},
            },
        }
        response = generate_response(schema)
        assert isinstance(response, dict)
        assert len(response) == 4
        assert isinstance(response["username"], str)
        assert isinstance(response["count"], int)
        assert isinstance(response["rating"], (int, float))
        assert isinstance(response["active"], bool)


class TestRejectObjectSchemaMissingProperties:
    def test_reject_object_schema_missing_properties_field(self):
        """Reject object schema missing properties field"""
        schema = {"type": "object"}
        with pytest.raises(ResponseGenerationError):
            generate_response(schema)


class TestHandleEmptyProperties:
    def test_handle_empty_properties_object(self):
        """Handle empty properties object"""
        schema = {"type": "object", "properties": {}}
        response = generate_response(schema)
        assert isinstance(response, dict)
        assert len(response) == 0
