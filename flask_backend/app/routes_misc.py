from datetime import datetime, timezone
from flask import Blueprint, jsonify, request

misc_bp = Blueprint("misc", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@misc_bp.get("/time")
def server_time():
    """Return current server UTC time."""
    now = datetime.now(timezone.utc).isoformat()
    return jsonify({"time_utc": now})

# PUBLIC_INTERFACE
@misc_bp.route("/echo", methods=["GET", "POST"])
def echo():
    """Echo back basic request info for debugging."""
    return jsonify({
        "method": request.method,
        "args": request.args.to_dict(flat=True),
        "json": request.get_json(silent=True),
        "headers": {k: v for k, v in request.headers.items() if k.lower() not in {"cookie", "authorization"}}
    })
