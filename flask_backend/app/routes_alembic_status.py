import subprocess
from flask import Blueprint, jsonify

alembic_status_bp = Blueprint("alembic_status", __name__, url_prefix="/diag")

# PUBLIC_INTERFACE
@alembic_status_bp.get("/alembic_current")
def alembic_current():
    """Return Alembic current revision output for diagnostics."""
    try:
        out = subprocess.check_output(["alembic", "current"], stderr=subprocess.STDOUT, text=True, timeout=8)
        return jsonify({"status": "ok", "output": out})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500
