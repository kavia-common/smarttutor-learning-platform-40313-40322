# PUBLIC_INTERFACE
def get_extra_paths_headers() -> dict:
    """Extra OpenAPI paths for headers diagnostics."""
    return {
        "/diag/headers": {
            "get": {
                "summary": "Echo request headers",
                "tags": ["headers"],
                "responses": {
                    "200": {"description": "Headers JSON"}
                }
            }
        }
    }
