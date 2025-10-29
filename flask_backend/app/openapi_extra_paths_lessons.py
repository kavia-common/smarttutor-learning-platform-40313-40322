# PUBLIC_INTERFACE
def get_extra_paths_lessons() -> dict:
    """Extra OpenAPI paths for listing lessons (dev/diagnostics)."""
    return {
        "/api/lessons": {
            "get": {
                "summary": "List lessons (dev-only)",
                "tags": ["core"],
                "parameters": [
                    {"name": "course_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "q", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of lessons with pagination"}},
            }
        }
    }
