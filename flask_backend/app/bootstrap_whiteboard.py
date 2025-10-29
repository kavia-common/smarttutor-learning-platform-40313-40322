from flask import Flask

# PUBLIC_INTERFACE
def register_whiteboard_if_available(app: Flask) -> None:
    """Attempt to register whiteboard routes if module is available."""
    try:
        from .register_whiteboard import register_whiteboard_routes
        register_whiteboard_routes(app)
    except Exception:
        pass
