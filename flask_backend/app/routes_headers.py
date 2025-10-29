from flask import Blueprint, jsonify, request

headers_bp = Blueprint("headers", __name__, url_prefix="/diag")

# PUBLIC_INTERFACE
@headers_bp.get("/headers")
def echo_headers():
    """Return request headers for diagnostics."""
    return jsonify({k: v for k, v in request.headers.items()})
