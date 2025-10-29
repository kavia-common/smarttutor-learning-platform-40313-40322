import os
from flask import Blueprint, jsonify, current_app

version_bp = Blueprint("version", __name__, url_prefix="/diag")

# PUBLIC_INTERFACE
@version_bp.get("/version")
def version():
    """Return application version and minimal environment presence checks."""
    return jsonify({
        "app_version": current_app.config.get("APP_VERSION", "0.1.0"),
        "has_database_url": bool(os.getenv("DATABASE_URL")),
        "has_jwt_secret": bool(os.getenv("JWT_SECRET")),
    })
