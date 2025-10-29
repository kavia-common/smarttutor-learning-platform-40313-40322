from flask import Flask
from .api import api
from .bootstrap import init_extensions

def register_all(app: Flask) -> None:
    """Register blueprints and initialize extensions."""
    init_extensions(app)
    app.register_blueprint(api)
