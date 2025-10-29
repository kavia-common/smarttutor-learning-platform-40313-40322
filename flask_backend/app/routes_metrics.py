from collections import Counter
from flask import Blueprint, jsonify, request, current_app

metrics_bp = Blueprint("metrics", __name__, url_prefix="/api")
_request_counts = Counter()

@metrics_bp.before_app_request
def _count_requests():
    # Count by endpoint path (coarse)
    path = request.path
    # Only count API endpoints to avoid noise
    if path.startswith("/api") or path == "/health":
        _request_counts[path] += 1

# PUBLIC_INTERFACE
@metrics_bp.get("/metrics")
def metrics():
    """
    summary: In-memory request counters
    description: Returns in-memory request counts by path for basic diagnostics (non-persistent).
    responses:
      200:
        description: Metrics payload
    """
    return jsonify({"counts": dict(_request_counts)})
