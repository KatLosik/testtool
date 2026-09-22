"""HTTP mock server for OpenAPI specifications."""

from flask import Flask, jsonify

from testtool.response_generator import ResponseGenerationError, generate_response


def create_app(spec: dict) -> Flask:
    """
    Create a Flask app that serves mock responses for an OpenAPI spec.

    Args:
        spec: Loaded OpenAPI specification dictionary

    Returns:
        Flask application configured with routes from the spec
    """
    app = Flask(__name__)

    paths = spec.get('paths', {})

    for path, methods in paths.items():
        for method, operation in methods.items():
            if method not in ('get', 'post', 'put', 'delete', 'patch'):
                continue

            response_schema = _extract_response_schema(operation)

            if response_schema is None:
                continue

            route_name = _make_route_name(path, method)

            view_func = _create_view_function(response_schema)

            app.add_url_rule(
                path,
                route_name,
                view_func,
                methods=[method.upper()],
            )

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({}), 404

    return app


def _extract_response_schema(operation: dict) -> dict | None:
    """Extract the response schema from an operation."""
    responses = operation.get('responses', {})

    response_200 = responses.get('200')
    if response_200 is None:
        return None

    content = response_200.get('content', {})
    json_content = content.get('application/json')
    if json_content is None:
        return None

    schema = json_content.get('schema')
    return schema


def _make_route_name(path: str, method: str) -> str:
    """Create a unique route name from path and method."""
    return f"{method}_{path.replace('/', '_')}"


def _create_view_function(schema: dict):
    """Create a view function that generates responses from a schema."""

    def view_func():
        try:
            response_data = generate_response(schema)
            return jsonify(response_data), 200
        except ResponseGenerationError:
            return jsonify({}), 500

    return view_func
