from flask import Flask

# PUBLIC_INTERFACE
def enable_cors(app: Flask) -> None:
    """Enable permissive CORS for local development.
    Note: tighten this in production.
    """
    try:
        # Lightweight manual headers without extra dependency
        @app.after_request
        def add_cors_headers(response):
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            return response
    except Exception:
        # Non-fatal if something goes wrong
        pass
