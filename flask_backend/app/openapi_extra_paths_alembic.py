# PUBLIC_INTERFACE
def get_extra_paths_alembic() -> dict:
    """Extra OpenAPI paths for Alembic diagnostics."""
    return {
        "/diag/alembic": {
            "get": {
                "summary": "Alembic status (placeholder)",
                "tags": ["alembic"],
                "responses": {
                    "200": {"description": "Status JSON"}
                }
            }
        }
    }
