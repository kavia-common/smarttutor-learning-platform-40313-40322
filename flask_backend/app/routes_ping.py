from flask import Blueprint, jsonify

ping_bp = Blueprint("ping", __name__, url_prefix="/diag")

# PUBLIC_INTERFACE
@ping_bp.get("/ping")
def ping():
    """Simple ping endpoint returning pong."""
    return jsonify({"pong": True})
