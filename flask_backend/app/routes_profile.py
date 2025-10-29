from flask import Blueprint, jsonify, g
from .auth_decorators import login_required
from .models import User

profile_bp = Blueprint("profile", __name__, url_prefix="/api/profile")

# PUBLIC_INTERFACE
@profile_bp.get("/")
@login_required
def me():
    """Return current authenticated user's profile."""
    uid = g.current_user_id
    u = User.query.get(uid)
    if not u:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"id": u.id, "email": u.email, "name": u.name, "role": u.role})
