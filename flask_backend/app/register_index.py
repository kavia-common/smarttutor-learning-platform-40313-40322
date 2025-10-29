from flask import Flask
from .routes_index import index_bp

# PUBLIC_INTERFACE
def register_index(app: Flask) -> None:
    """Register root index route blueprint."""
    app.register_blueprint(index_bp)
