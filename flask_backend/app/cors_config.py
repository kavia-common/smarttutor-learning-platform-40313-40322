import os
from typing import Any, Dict

def build_cors_resources() -> Dict[str, Dict[str, Any]]:
    """Build CORS resources mapping from env ALLOWED_ORIGINS (comma-separated).
    Defaults to allow-all in dev if not set."""
    allowed = os.getenv("ALLOWED_ORIGINS", "").strip()
    if not allowed:
        # Dev-friendly default; set ALLOWED_ORIGINS in production.
        return {r"/api/*": {"origins": "*"}}
    origins = [o.strip() for o in allowed.split(",") if o.strip()]
    return {r"/api/*": {"origins": origins}}
