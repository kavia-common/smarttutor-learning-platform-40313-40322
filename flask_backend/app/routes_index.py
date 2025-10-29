from flask import Blueprint, jsonify

index_bp = Blueprint("index", __name__)

# PUBLIC_INTERFACE
@index_bp.get("/")
def index():
    """Index route listing helpful diagnostics and docs endpoints."""
    return jsonify({
        "service": "SmartTutor Flask Backend",
        "links": {
            "health": "/health",
            "openapi": "/openapi.json",
            "docs_redoc": "/docs/openapi.html",
            "diag_ping": "/diag/ping",
            "diag_headers": "/diag/headers",
            "diag_alembic": "/diag/alembic",
            "diag_version": "/diag/version",
            "whiteboard_sessions": "/api/whiteboard/sessions",
        }
    })
