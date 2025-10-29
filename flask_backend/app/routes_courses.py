from flask import Blueprint, jsonify, request
from app.db import db
from app.models import Course

courses_bp = Blueprint("courses", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@courses_bp.get("/courses")
def list_courses():
    """List courses (read-only, dev/diagnostics).

    Query params:
    - q: optional search in title (case-insensitive)
    - limit: max items (default 50, max 200)
    - offset: offset for pagination (default 0)
    """
    q = (request.args.get("q") or "").strip()
    limit = min(max(request.args.get("limit", type=int) or 50, 1), 200)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    query = db.session.query(Course)
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(
            db.func.lower(Course.title).like(like),
        )
    total = query.count()
    rows = (
        query.order_by(Course.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "created_at": c.created_at.isoformat() if c.created_at else None,
        }
        for c in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
