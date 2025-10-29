from flask import Blueprint, jsonify, request

echo_bp = Blueprint("echo", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@echo_bp.any("/echo")
def echo():
    """
    summary: Echo request info (debug)
    description: Returns method, headers (sanitized), query params, and JSON body to aid debugging.
    responses:
      200:
        description: Echo payload
    """
    # Sanitize headers by removing Authorization
    headers = {k: v for k, v in request.headers.items() if k.lower() != "authorization"}
    payload = {
        "method": request.method,
        "path": request.path,
        "args": request.args.to_dict(flat=False),
        "headers": headers,
        "json": request.get_json(silent=True),
    }
    return jsonify(payload)
