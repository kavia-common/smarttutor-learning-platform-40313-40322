import os
import threading
from flask import Blueprint, jsonify

proc_bp = Blueprint("proc", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@proc_bp.get("/proc")
def proc_info():
    """
    summary: Process diagnostics
    description: Returns current process ID and active thread count for quick diagnostics.
    responses:
      200:
        description: Process diagnostics payload
    """
    return jsonify({"pid": os.getpid(), "threads": threading.active_count()})
