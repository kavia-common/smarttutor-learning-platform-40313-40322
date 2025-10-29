import os
from app import create_app
from app.bootstrap import bootstrap_extras
from app.bootstrap_index import register_index_if_available
from app.logging_setup import setup_logging
from app.bootstrap_whiteboard import register_whiteboard_if_available

# PUBLIC_INTERFACE
def get_app():
    """WSGI factory to create the Flask app."""
    app = create_app()
    # Apply optional extras (CORS, headers)
    try:
        bootstrap_extras(app)
    except Exception:
        pass
    # Setup logging and error handler
    try:
        setup_logging(app)
    except Exception:
        pass
    # Register root index route if available
    try:
        register_index_if_available(app)
    except Exception:
        pass
    # Register whiteboard routes if available
    try:
        register_whiteboard_if_available(app)
    except Exception:
        pass
    return app

# Default app for WSGI servers
app = get_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)
