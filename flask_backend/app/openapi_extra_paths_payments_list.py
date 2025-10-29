# PUBLIC_INTERFACE
def get_extra_paths_payments_list() -> dict:
    """Extra OpenAPI path for listing payments (dev/diagnostics)."""
    return {
        "/api/payments": {
            "get": {
                "summary": "List payments (dev-only)",
                "tags": ["payments"],
                "parameters": [
                    {"name": "user_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "course_id", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "status", "in": "query", "required": False, "schema": {"type": "string"}},
                    {"name": "limit", "in": "query", "required": False, "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "required": False, "schema": {"type": "integer"}},
                ],
                "responses": {"200": {"description": "List of payments with pagination"}},
            }
        }
    }
