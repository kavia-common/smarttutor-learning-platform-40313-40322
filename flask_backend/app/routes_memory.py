import os
import resource
from flask import Blueprint, jsonify

memory_bp = Blueprint("memory", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@memory_bp.get("/memory")
def memory():
    """
    summary: Service memory usage
    description: Returns the current process's resident set size (RSS) in kilobytes.
    responses:
      200:
        description: Memory usage payload
    """
    usage = resource.getrusage(resource.RUSAGE_SELF)
    rss_kb = getattr(usage, "ru_maxrss", 0)
    # On some platforms ru_maxrss is in bytes; standardize to kilobytes if too large
    if rss_kb > 1_000_000_000:  # extremely large -> likely bytes
        rss_kb = rss_kb // 1024
    return jsonify({"rss_kb": int(rss_kb), "pid": os.getpid()})
