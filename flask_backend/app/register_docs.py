from flask import Flask
from .openapi import openapi_bp
from .docs import docs_bp

def register_docs(app: Flask) -> None:
    """Register documentation-related blueprints like OpenAPI and docs."""
    app.register_blueprint(openapi_bp)
    app.register_blueprint(docs_bp)
