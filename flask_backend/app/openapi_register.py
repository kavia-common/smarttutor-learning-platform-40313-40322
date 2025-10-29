"""
OpenAPI registrar.

Assemble a minimal OpenAPI document and merge extra path providers if present.
"""

from typing import Dict, Any
from flask import Flask

def _base_spec(app: Flask) -> Dict[str, Any]:
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "SmartTutor API",
            "version": app.config.get("APP_VERSION", "0.1.0"),
            "description": "REST API for SmartTutor platform",
        },
        "tags": [
            {"name": "core", "description": "Core endpoints"},
            {"name": "payments", "description": "Payments and receipts"},
            {"name": "whiteboard", "description": "Whiteboard realtime/session APIs"},
            {"name": "alembic", "description": "Database migrations diagnostics"},
            {"name": "headers", "description": "Diagnostics headers echo"},
        ],
        "paths": {
            "/health": {
                "get": {
                    "summary": "Health check",
                    "tags": ["core"],
                    "responses": {"200": {"description": "OK"}},
                }
            }
        },
        "components": {"schemas": {}},
    }

# PUBLIC_INTERFACE
def build_openapi(app: Flask) -> Dict[str, Any]:
    """Build the OpenAPI spec and merge extra paths from modular providers."""
    spec = _base_spec(app)

    # Merge alembic paths
    try:
        from .openapi_extra_paths_alembic import get_extra_paths_alembic  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_alembic() or {})
    except Exception:
        pass

    # Merge headers paths
    try:
        from .openapi_extra_paths_headers import get_extra_paths_headers  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_headers() or {})
    except Exception:
        pass

    # Merge whiteboard paths
    try:
        from .openapi_extra_paths_whiteboard import get_extra_paths_whiteboard  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_whiteboard() or {})
    except Exception:
        pass

    # Merge payments placeholder extra paths (if present)
    try:
        from .openapi_extra_paths_payments import get_extra_paths_payments  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_payments() or {})
    except Exception:
        pass

    # Merge payment receipt path
    try:
        from .openapi_extra_paths_payment_receipt import get_extra_paths_payment_receipt  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_payment_receipt() or {})
    except Exception:
        pass

    # Merge version path
    try:
        from .openapi_extra_paths_version import get_extra_paths_version  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_version() or {})
    except Exception:
        pass

    # Merge index path
    try:
        from .openapi_extra_paths_index import get_extra_paths_index  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_index() or {})
    except Exception:
        pass

    # Merge users (dev) path
    try:
        from .openapi_extra_paths_users import get_extra_paths_users  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_users() or {})
    except Exception:
        pass

    # Merge courses (dev) path
    try:
        from .openapi_extra_paths_courses import get_extra_paths_courses  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_courses() or {})
    except Exception:
        pass

    # Merge enrollments (dev) path
    try:
        from .openapi_extra_paths_enrollments import get_extra_paths_enrollments  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_enrollments() or {})
    except Exception:
        pass

    # Merge payments list (dev) path
    try:
        from .openapi_extra_paths_payments_list import get_extra_paths_payments_list  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_payments_list() or {})
    except Exception:
        pass

    # Merge recommendations cache (dev) path
    try:
        from .openapi_extra_paths_recommendations import get_extra_paths_recommendations  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_recommendations() or {})
    except Exception:
        pass

    # Merge lessons (dev) path
    try:
        from .openapi_extra_paths_lessons import get_extra_paths_lessons  # type: ignore
        spec.setdefault("paths", {}).update(get_extra_paths_lessons() or {})
    except Exception:
        pass

    return spec
