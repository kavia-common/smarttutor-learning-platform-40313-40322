# PUBLIC_INTERFACE
def get_extra_paths_version() -> dict:
    """Extra OpenAPI paths for a version endpoint."""
    return {
        "/diag/version": {
            "get": {
                "summary": "Application version and env presence check",
                "tags": ["core"],
                "responses": {
                    "200": {"description": "Version JSON"}
                }
            }
        }
    }
