from flask import Flask
from .routes_memory import memory_bp

# PUBLIC_INTERFACE
def register_memory_routes(app: Flask) -> None:
    """Register memory diagnostics blueprint."""
    app.register_blueprint(memory_bp)
