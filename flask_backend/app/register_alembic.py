from flask import Flask

# PUBLIC_INTERFACE
def register_alembic_routes(app: Flask) -> None:
    """Register Alembic diagnostics routes with the Flask app."""
    try:
        from .routes_alembic_status import alembic_status_bp  # type: ignore
        app.register_blueprint(alembic_status_bp)
    except Exception:
        # Non-fatal: tools may not be present in some environments
        pass
