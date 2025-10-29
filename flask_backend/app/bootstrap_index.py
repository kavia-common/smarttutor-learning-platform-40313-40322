from flask import Flask

# PUBLIC_INTERFACE
def register_index_if_available(app: Flask) -> None:
    """Attempt to register the index route if module is available."""
    try:
        from .register_index import register_index
        register_index(app)
    except Exception:
        # Safe no-op if import fails
        pass
