from functools import wraps
from typing import Callable, Optional
from flask import request, jsonify, current_app, g
from .security import verify_jwt

def _get_bearer_token() -> Optional[str]:
    auth = request.headers.get("Authorization", "")
    if not auth.lower().startswith("bearer "):
        return None
    return auth.split(" ", 1)[1].strip()

# PUBLIC_INTERFACE
def login_required(fn: Callable):
    """Decorator to require a valid JWT in Authorization: Bearer header.

    On success, sets g.current_user_id and g.current_email.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = _get_bearer_token()
        if not token:
            return jsonify({"error": "missing bearer token"}), 401
        claims = verify_jwt(token, current_app.config["JWT_SECRET"])
        if not claims:
            return jsonify({"error": "invalid or expired token"}), 401
        g.current_user_id = claims.get("sub")
        g.current_email = claims.get("email")
        return fn(*args, **kwargs)
    return wrapper
