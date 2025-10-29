from flask import Flask
from .openapi_download import openapi_dl_bp

def register_openapi_download(app: Flask) -> None:
    """Register the OpenAPI download endpoint."""
    app.register_blueprint(openapi_dl_bp)
