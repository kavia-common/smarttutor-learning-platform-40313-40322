"""
Route registrar for modular blueprints.

This module attempts to import and register optional route blueprints so the app
can function even if some modules are not present during early development.
"""
from flask import Flask

# PUBLIC_INTERFACE
def register_all_routes(app: Flask) -> None:
    """Register all known blueprints if available.

    Tries to import modules and register their blueprints. Missing modules are ignored
    to keep development flexible.
    """
    # Diagnostics headers routes
    try:
        from .routes_headers import headers_bp  # type: ignore
        app.register_blueprint(headers_bp)
    except Exception:
        pass

    # Alembic/status routes
    try:
        from .routes_alembic import alembic_bp  # type: ignore
        app.register_blueprint(alembic_bp)
    except Exception:
        pass

    # Whiteboard routes
    try:
        from .routes_whiteboard import whiteboard_bp  # type: ignore
        app.register_blueprint(whiteboard_bp)
    except Exception:
        pass

    # Payment receipt (read-only dev tool)
    try:
        from .routes_payment_receipt import receipt_bp  # type: ignore
        app.register_blueprint(receipt_bp)
    except Exception:
        pass

    # Ping
    try:
        from .routes_ping import ping_bp  # type: ignore
        app.register_blueprint(ping_bp)
    except Exception:
        pass

    # Version
    try:
        from .routes_version import version_bp  # type: ignore
        app.register_blueprint(version_bp)
    except Exception:
        pass

    # Index
    try:
        from .routes_index import index_bp  # type: ignore
        app.register_blueprint(index_bp)
    except Exception:
        pass

    # Users (dev read-only)
    try:
        from .routes_users import users_bp  # type: ignore
        app.register_blueprint(users_bp)
    except Exception:
        pass

    # Courses (dev read-only)
    try:
        from .routes_courses import courses_bp  # type: ignore
        app.register_blueprint(courses_bp)
    except Exception:
        pass

    # Enrollments (dev read-only)
    try:
        from .routes_enrollments import enrollments_bp  # type: ignore
        app.register_blueprint(enrollments_bp)
    except Exception:
        pass

    # Payments (dev read-only)
    try:
        from .routes_payments import payments_bp  # type: ignore
        app.register_blueprint(payments_bp)
    except Exception:
        pass

    # Docs (serve Redoc HTML)
    try:
        from .routes_docs import docs_bp  # type: ignore
        app.register_blueprint(docs_bp)
    except Exception:
        pass

    # Recommendations cache (dev read-only)
    try:
        from .routes_recommendations import recommendations_bp  # type: ignore
        app.register_blueprint(recommendations_bp)
    except Exception:
        pass

    # Lessons (dev read-only)
    try:
        from .routes_lessons import lessons_bp  # type: ignore
        app.register_blueprint(lessons_bp)
    except Exception:
        pass
