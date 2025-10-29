# Loader to apply OpenAPI path patches modularly.
def apply_patches(spec: dict) -> None:
    try:
        from .openapi_register_users_patch import merge_users_paths  # type: ignore
        merge_users_paths(spec)
    except Exception:
        pass
    try:
        from .openapi_register_alembic_patch import merge_alembic_paths  # type: ignore
        merge_alembic_paths(spec)
    except Exception:
        pass
