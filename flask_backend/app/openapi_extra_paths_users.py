# PUBLIC_INTERFACE
def get_extra_paths_users() -> dict:
    """Extra OpenAPI paths for listing users (dev/diagnostics)."""
    return {
        "/api/users": {
            "get": {
                "summary": "List users (dev-only)",
                "tags": ["core"],
                "parameters": [
                    {"name": "q", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of users with pagination"}},
            }
        }
    }
