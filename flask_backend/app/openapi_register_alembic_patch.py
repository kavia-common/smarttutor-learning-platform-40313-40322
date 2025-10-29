# Patch to merge Alembic diagnostics OpenAPI paths into the main spec.

def merge_alembic_paths(spec: dict) -> None:
    try:
        from .openapi_extra_paths_alembic import get_extra_paths_alembic  # type: ignore
        extra = get_extra_paths_alembic() or {}
        spec.setdefault("paths", {}).update(extra)
    except Exception:
        pass
