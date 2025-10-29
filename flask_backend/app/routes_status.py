from flask import Blueprint, jsonify
from .constants import APP_NAME, APP_VERSION

status_bp = Blueprint("status", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@status_bp.get("/status")
def status():
    """
    summary: Backend status
    description: Returns service name, version, and a simple ok flag for readiness checks.
    responses:
      200:
        description: Status payload
    """
    return jsonify({"ok": True, "name": APP_NAME, "version": APP_VERSION})
