# PUBLIC_INTERFACE
def get_extra_paths_enrollments() -> dict:
    """Extra OpenAPI paths for listing enrollments (dev/diagnostics)."""
    return {
        "/api/enrollments": {
            "get": {
                "summary": "List enrollments (dev-only)",
                "tags": ["core"],
                "parameters": [
                    {"name": "user_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "course_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of enrollments with pagination"}},
            }
        }
    }
