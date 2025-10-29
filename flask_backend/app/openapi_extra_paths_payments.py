# PUBLIC_INTERFACE
def get_extra_paths_payments() -> dict:
    """Extra OpenAPI placeholder paths for payments."""
    return {
        "/api/payments": {
            "get": {
                "summary": "List payments (placeholder)",
                "tags": ["payments"],
                "responses": {"200": {"description": "List of payments (not implemented)"}}
            }
        }
    }
