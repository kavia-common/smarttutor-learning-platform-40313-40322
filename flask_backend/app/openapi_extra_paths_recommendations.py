# PUBLIC_INTERFACE
def get_extra_paths_recommendations() -> dict:
    """Extra OpenAPI paths for listing recommendations cache (dev/diagnostics)."""
    return {
        "/api/recommendations/cache": {
            "get": {
                "summary": "List recommendations cache (dev-only)",
                "tags": ["core"],
                "parameters": [
                    {"name": "user_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of recommendation cache entries"}},
            }
        }
    }
