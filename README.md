# OpenAPI Mock Server

A Python tool that generates dynamic API responses from OpenAPI/Swagger specifications.

## What It Does

Load an OpenAPI specification file and start an HTTP mock server that:
- Accepts GET requests to endpoints defined in the spec
- Generates mock response data matching the response schema
- Returns JSON responses with appropriate HTTP status codes

Perfect for testing applications without a real backend.

## Setup

1. Create a Python virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **Linux/macOS**: `source .venv/bin/activate`
   - **Windows**: `.venv\Scripts\activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

Start the mock server with an OpenAPI spec file:

```
python -m testtool --spec input/example.yaml --port 5000
```

Arguments:
- `--spec` (required): Path to OpenAPI specification file (YAML or JSON)
- `--port` (optional): Port to listen on (default: 5000)

## Example Usage

With the server running on `http://localhost:5000`, try these requests:

```bash
# Get a greeting string
curl http://localhost:5000/greeting

# Get a user object
curl http://localhost:5000/user

# Get an array of tags
curl http://localhost:5000/tags

# Get 404 for unmapped endpoint
curl http://localhost:5000/nonexistent
```

## Supported Features

- **Spec formats**: OpenAPI 3.0.0, Swagger 2.0 (YAML and JSON)
- **Response types**: Primitive types (string, integer, number, boolean), objects, arrays
- **HTTP methods**: GET requests only
- **Status codes**: 200 for matched endpoints, 404 for unmapped paths
- **Response format**: JSON with `Content-Type: application/json` header

## Not Supported

- POST, PUT, DELETE, PATCH methods
- Path parameters (e.g., `/users/{id}`)
- Query parameters
- Request body validation
- Authentication/authorization
- Custom status codes (only 200 and 404)
- Advanced OpenAPI features ($ref, allOf, oneOf, etc.)

## Example Specification

See `input/example.yaml` for a complete example with multiple endpoint types.