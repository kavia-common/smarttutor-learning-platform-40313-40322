from flask import Flask
from .config import get_config
from .db import db

# PUBLIC_INTERFACE
def create_app() -> Flask:
    """Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    cfg = get_config()
    app.config.from_mapping(cfg)

    # Configure logging and print startup banner
    try:
        from .logging_config import configure_logging
        configure_logging()
    except Exception:
        pass
    try:
        from .startup import print_startup_banner
        print_startup_banner()
    except Exception:
        pass

    # Enable CORS for local development
    try:
        from .cors import enable_cors
        enable_cors(app)
    except Exception:
        pass

    # Initialize DB
    db.init_app(app)

    # Ensure models are imported so Alembic can autogenerate properly
    with app.app_context():
        from .models import (  # noqa: F401
            user, course, lesson, enrollment, chat_message,
            whiteboard_session, whiteboard_event, payment, recommendations_cache
        )

    # Register all optional routes in one place
    try:
        from .register_routes import register_all
        register_all(app)
    except Exception:
        pass

    # Register Alembic diagnostics
    try:
        from .register_alembic import register_alembic_routes
        register_alembic_routes(app)
    except Exception:
        pass
    # Also include versions endpoints explicitly
    try:
        from .routes_versions import versions_bp
        app.register_blueprint(versions_bp)
    except Exception:
        pass

    # Register OpenAPI endpoint if builder/register is present
    try:
        from .openapi_register import register_openapi
        register_openapi(app)
    except Exception:
        pass

    # Register modular routes if available
    try:
        from .register_routes import register_all_routes
        register_all_routes(app)
    except Exception:
        pass
    # Register Alembic diagnostics
    try:
        from .register_alembic import register_alembic_routes
        register_alembic_routes(app)
    except Exception:
        pass

    # OpenAPI JSON route
    try:
        from .openapi_register import build_openapi
        @app.get("/openapi.json")
        def openapi_json():
            """Return the OpenAPI specification JSON."""
            return build_openapi(app)
    except Exception:
        pass

    # Simple health check for now
    @app.get("/health")
    def health():
        """Health check endpoint."""
        return {"status": "ok"}

    return app
