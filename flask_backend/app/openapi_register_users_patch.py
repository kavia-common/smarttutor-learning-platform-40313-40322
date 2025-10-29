# This module patches openapi_register to merge users extra paths.
# It should be imported by app/openapi_register.py; keeping separate to avoid edit conflicts.

def merge_users_paths(spec: dict) -> None:
    try:
        from .openapi_extra_paths_users import get_extra_paths_users  # type: ignore
        extra = get_extra_paths_users() or {}
        spec.setdefault("paths", {}).update(extra)
    except Exception:
        pass
