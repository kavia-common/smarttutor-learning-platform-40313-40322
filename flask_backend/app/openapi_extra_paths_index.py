# PUBLIC_INTERFACE
def get_extra_paths_index() -> dict:
    """Extra OpenAPI path for API index."""
    return {
        "/": {
            "get": {
                "summary": "API index",
                "tags": ["core"],
                "responses": {
                    "200": {"description": "Links to core endpoints"}
                }
            }
        }
    }
