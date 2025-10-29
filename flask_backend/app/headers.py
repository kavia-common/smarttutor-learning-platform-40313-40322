from flask import Flask
from .constants import APP_NAME, APP_VERSION

# PUBLIC_INTERFACE
def register_response_headers(app: Flask) -> None:
    """Attach standard response headers for diagnostics."""
    @app.after_request
    def _add_headers(resp):
        resp.headers.setdefault("X-Service-Name", APP_NAME)
        resp.headers.setdefault("X-Service-Version", APP_VERSION)
        return resp
