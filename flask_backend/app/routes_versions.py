from flask import Blueprint, jsonify
import os

versions_bp = Blueprint("versions", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@versions_bp.get("/status")
def status():
    """Return basic service status with version."""
    return jsonify({"name": "smarttutor-backend", "version": os.getenv("APP_VERSION", "0.1.0"), "ok": True})

# PUBLIC_INTERFACE
@versions_bp.get("/version")
def version():
    """Return the backend version only."""
    return jsonify({"version": os.getenv("APP_VERSION", "0.1.0")})
