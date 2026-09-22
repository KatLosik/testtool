import tempfile
from pathlib import Path

import pytest


class TestLoadAndParseYAML:
    def test_load_and_parse_valid_yaml_openapi_spec(self):
        """Load and parse valid YAML OpenAPI spec"""
        yaml_content = """
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /users:
    get:
      responses:
        '200':
          description: Success
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(yaml_content)
            temp_path = f.name

        try:
            from testtool.spec_loader import load_spec
            spec = load_spec(temp_path)
            assert spec is not None
            assert spec['openapi'] == '3.0.0'
            assert spec['info']['title'] == 'Test API'
            assert '/users' in spec['paths']
        finally:
            Path(temp_path).unlink()


class TestLoadAndParseJSON:
    def test_load_and_parse_valid_json_openapi_spec(self):
        """Load and parse valid JSON OpenAPI spec"""
        json_content = """{
  "openapi": "3.0.0",
  "info": {
    "title": "Test API",
    "version": "1.0.0"
  },
  "paths": {
    "/users": {
      "get": {
        "responses": {
          "200": {
            "description": "Success"
          }
        }
      }
    }
  }
}"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write(json_content)
            temp_path = f.name

        try:
            from testtool.spec_loader import load_spec
            spec = load_spec(temp_path)
            assert spec is not None
            assert spec['openapi'] == '3.0.0'
            assert spec['info']['title'] == 'Test API'
            assert '/users' in spec['paths']
        finally:
            Path(temp_path).unlink()


class TestRejectMalformedYAML:
    def test_reject_malformed_yaml_with_clear_error(self):
        """Reject malformed YAML with clear error"""
        yaml_content = """
openapi: 3.0.0
info:
  title: Test API
  invalid: [unclosed list
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(yaml_content)
            temp_path = f.name

        try:
            from testtool.spec_loader import SpecLoadError, load_spec
            with pytest.raises(SpecLoadError):
                load_spec(temp_path)
        finally:
            Path(temp_path).unlink()


class TestRejectMalformedJSON:
    def test_reject_malformed_json_with_clear_error(self):
        """Reject malformed JSON with clear error"""
        json_content = """{
  "openapi": "3.0.0",
  "info": {
    "title": "Test API"
    "version": "1.0.0"
  }
}"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write(json_content)
            temp_path = f.name

        try:
            from testtool.spec_loader import SpecLoadError, load_spec
            with pytest.raises(SpecLoadError):
                load_spec(temp_path)
        finally:
            Path(temp_path).unlink()


class TestHandleMissingFile:
    def test_handle_nonexistent_file_with_clear_error(self):
        """Handle nonexistent file with clear error"""
        from testtool.spec_loader import SpecLoadError, load_spec
        with pytest.raises(SpecLoadError):
            load_spec('/nonexistent/path/to/spec.yaml')
