from flask import Flask
from .routes_whiteboard import whiteboard_bp

# PUBLIC_INTERFACE
def register_whiteboard_routes(app: Flask) -> None:
    """Register whiteboard sessions and events routes."""
    app.register_blueprint(whiteboard_bp)
