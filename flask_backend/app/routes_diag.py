import os
import time
import json
from dataclasses import asdict, dataclass
from flask import Blueprint, jsonify, current_app

_started_at = time.time()
diag_bp = Blueprint("diag", __name__, url_prefix="/api")

@dataclass
class UptimePayload:
    started_at: float
    now: float
    uptime_seconds: float

# PUBLIC_INTERFACE
@diag_bp.get("/uptime")
def uptime():
    """Service uptime information."""
    now = time.time()
    payload = UptimePayload(started_at=_started_at, now=now, uptime_seconds=now - _started_at)
    return jsonify(asdict(payload))

def _read_proc_status_rss_kb():
    try:
        with open("/proc/self/status", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    # e.g., ['VmRSS:', '123456', 'kB']
                    return int(parts[1])
    except Exception:
        return None
    return None

# PUBLIC_INTERFACE
@diag_bp.get("/memory")
def memory():
    """Return memory RSS in KB if available (Linux), else null."""
    rss_kb = _read_proc_status_rss_kb()
    return jsonify({"rss_kb": rss_kb})
