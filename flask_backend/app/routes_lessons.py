from flask import Blueprint, jsonify, request
from app.db import db
from app.models import Lesson, Course

lessons_bp = Blueprint("lessons", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@lessons_bp.get("/lessons")
def list_lessons():
    """List lessons (read-only, dev/diagnostics).

    Query params:
    - course_id: optional filter by course
    - q: optional search by title (case-insensitive)
    - limit: max items (default 100, max 500)
    - offset: offset for pagination (default 0)
    """
    course_id = request.args.get("course_id", type=int)
    q = (request.args.get("q") or "").strip()
    limit = min(max(request.args.get("limit", type=int) or 100, 1), 500)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    query = db.session.query(Lesson, Course).join(Course, Lesson.course_id == Course.id)

    if course_id:
        query = query.filter(Lesson.course_id == course_id)

    if q:
        like = f"%{q.lower()}%"
        query = query.filter(db.func.lower(Lesson.title).like(like))

    total = query.count()
    rows = (
        query.order_by(Lesson.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": l.id,
            "title": l.title,
            "content": l.content,
            "video_url": l.video_url,
            "created_at": l.created_at.isoformat() if l.created_at else None,
            "course": {"id": c.id, "title": c.title},
        }
        for (l, c) in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
