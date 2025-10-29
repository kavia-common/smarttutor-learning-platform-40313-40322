from flask import Blueprint, jsonify, request
from app.db import db
from app.models import User

users_bp = Blueprint("users", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@users_bp.get("/users")
def list_users():
    """List users (read-only, dev/diagnostics).

    Query params:
    - q: optional search in email or name (case-insensitive)
    - limit: max items (default 50, max 200)
    - offset: offset for pagination (default 0)
    """
    q = (request.args.get("q") or "").strip()
    limit = min(max(request.args.get("limit", type=int) or 50, 1), 200)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    query = db.session.query(User)
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(
            db.or_(
                db.func.lower(User.email).like(like),
                db.func.lower(User.name).like(like),
            )
        )
    total = query.count()
    rows = (
        query.order_by(User.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": u.id,
            "email": u.email,
            "name": u.name,
            "role": u.role,
            "created_at": u.created_at.isoformat() if u.created_at else None,
        }
        for u in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
