from flask import Flask
from .routes_cpu import cpu_bp

# PUBLIC_INTERFACE
def register_cpu_routes(app: Flask) -> None:
    """Register CPU diagnostics blueprint."""
    app.register_blueprint(cpu_bp)
