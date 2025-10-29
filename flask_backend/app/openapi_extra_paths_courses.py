# PUBLIC_INTERFACE
def get_extra_paths_courses() -> dict:
    """Extra OpenAPI paths for listing courses (dev/diagnostics)."""
    return {
        "/api/courses": {
            "get": {
                "summary": "List courses (dev-only)",
                "tags": ["core"],
                "parameters": [
                    {"name": "q", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of courses with pagination"}},
            }
        }
    }
