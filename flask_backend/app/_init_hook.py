from flask import Flask
from .register_routes import register_routes
from .register_memory import register_memory_routes
from .register_cpu import register_cpu_routes
from .register_cpu import register_cpu_routes

# PUBLIC_INTERFACE
def run(app: Flask) -> None:
    """Attach routes to app."""
    register_routes(app)
    register_memory_routes(app)
