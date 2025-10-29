import os
from flask import Blueprint, jsonify

cpu_bp = Blueprint("cpu", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@cpu_bp.get("/cpu")
def cpu_info():
    """
    summary: CPU diagnostics
    description: Returns CPU count and system load averages (1m, 5m, 15m) if available.
    responses:
      200:
        description: CPU diagnostics payload
    """
    count = os.cpu_count() or 1
    loads = None
    try:
        loads = os.getloadavg()
    except Exception:
        loads = None
    return jsonify({
        "cpu_count": count,
        "load_avg": loads if loads is not None else []
    })
