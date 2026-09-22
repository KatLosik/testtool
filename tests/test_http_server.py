import tempfile
import threading
import time
from pathlib import Path

import pytest
import requests

from testtool.server import create_app
from testtool.spec_loader import load_spec


@pytest.fixture
def simple_spec_file():
    """Create a temporary OpenAPI spec file for testing."""
    spec_content = """
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /greeting:
    get:
      responses:
        '200':
          description: A greeting
          content:
            application/json:
              schema:
                type: string
  /user:
    get:
      responses:
        '200':
          description: A user object
          content:
            application/json:
              schema:
                type: object
                properties:
                  name:
                    type: string
                  age:
                    type: integer
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write(spec_content)
        temp_path = f.name
    yield temp_path
    Path(temp_path).unlink()


@pytest.fixture
def server(simple_spec_file):
    """Start the mock server for testing."""
    spec = load_spec(simple_spec_file)
    app = create_app(spec)
    app.config['TESTING'] = True

    server_thread = threading.Thread(
        target=lambda: app.run(host='127.0.0.1', port=5555, debug=False, use_reloader=False)
    )
    server_thread.daemon = True
    server_thread.start()
    time.sleep(0.5)

    yield app

    with app.app_context():
        pass


class TestGetRequestToUnmappedEndpoint:
    def test_server_responds_with_404_for_get_request_to_unmapped_endpoint(self, server):
        """Server responds with 404 for GET request to unmapped endpoint"""
        response = requests.get('http://127.0.0.1:5555/nonexistent')
        assert response.status_code == 404


class TestGetRequestToMappedEndpointWithStringResponse:
    def test_server_responds_with_200_and_json_for_mapped_endpoint_string_response(self, server):
        """Server responds with 200 and JSON for GET request to mapped endpoint with string response"""
        response = requests.get('http://127.0.0.1:5555/greeting')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, str)


class TestResponseContentTypeHeader:
    def test_server_responds_with_content_type_application_json_header(self, server):
        """Server responds with Content-Type: application/json header"""
        response = requests.get('http://127.0.0.1:5555/greeting')
        assert response.headers['Content-Type'] == 'application/json'


class TestGetRequestToMappedEndpointWithObjectResponse:
    def test_server_responds_with_200_and_json_for_mapped_endpoint_object_response(self, server):
        """Server responds with 200 and JSON for GET request to mapped endpoint with object response"""
        response = requests.get('http://127.0.0.1:5555/user')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert 'name' in data
        assert 'age' in data
        assert isinstance(data['name'], str)
        assert isinstance(data['age'], int)
