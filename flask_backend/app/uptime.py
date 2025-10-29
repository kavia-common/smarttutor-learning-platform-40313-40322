from __future__ import annotations
from datetime import datetime, timezone
from flask import Flask, Blueprint, jsonify

_started_at: datetime | None = None

def _now() -> datetime:
    return datetime.now(timezone.utc)

# PUBLIC_INTERFACE
def init_uptime(app: Flask) -> None:
    """Initialize uptime tracker and register uptime route."""
    global _started_at
    if _started_at is None:
        _started_at = _now()

    bp = Blueprint("uptime", __name__, url_prefix="/api")

    @bp.get("/uptime")
    def uptime():
        """Return service uptime seconds since process start."""
        assert _started_at is not None
        delta = (_now() - _started_at).total_seconds()
        return jsonify({"started_at": _started_at.isoformat(), "uptime_seconds": int(delta)})

    # Hidden reset endpoint for tests/dev only
    @bp.post("/uptime/reset")
    def uptime_reset():
        """Reset uptime start time (dev/test)."""
        global _started_at
        _started_at = _now()
        return jsonify({"reset": True, "started_at": _started_at.isoformat()})

    app.register_blueprint(bp)
