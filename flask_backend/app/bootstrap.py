from flask import Flask

# PUBLIC_INTERFACE
def bootstrap_extras(app: Flask) -> None:
    """Bootstrap optional extras like CORS and after_request hooks."""
    try:
        from .cors import enable_cors
        enable_cors(app)
    except Exception:
        pass
    try:
        from .after_request import register_after_request
        register_after_request(app)
    except Exception:
        pass
