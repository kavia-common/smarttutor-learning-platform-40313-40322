from flask import Blueprint, jsonify

alembic_bp = Blueprint("alembic", __name__, url_prefix="/diag")

# PUBLIC_INTERFACE
@alembic_bp.get("/alembic")
def alembic_status():
    """Return a simple status placeholder for Alembic diagnostics (expand later)."""
    return jsonify({"alembic": "ok"})
