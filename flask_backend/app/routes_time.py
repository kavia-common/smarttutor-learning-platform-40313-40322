from datetime import datetime, timezone
from flask import Blueprint, jsonify

time_bp = Blueprint("time", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@time_bp.get("/time")
def get_time():
    """
    summary: Server time
    description: Returns current server time in UTC ISO8601.
    responses:
      200:
        description: Time payload
    """
    now = datetime.now(timezone.utc).isoformat()
    return jsonify({"utc": now})
