from flask import Blueprint, jsonify, request
from app.db import db
from app.models import Enrollment, User, Course

enrollments_bp = Blueprint("enrollments", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@enrollments_bp.get("/enrollments")
def list_enrollments():
    """List enrollments (read-only, dev/diagnostics).

    Query params:
    - user_id: optional filter by user
    - course_id: optional filter by course
    - limit: max items (default 100, max 500)
    - offset: offset for pagination (default 0)
    """
    user_id = request.args.get("user_id", type=int)
    course_id = request.args.get("course_id", type=int)
    limit = min(max(request.args.get("limit", type=int) or 100, 1), 500)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    q = (
        db.session.query(Enrollment, User, Course)
        .join(User, Enrollment.user_id == User.id)
        .join(Course, Enrollment.course_id == Course.id)
    )
    if user_id:
        q = q.filter(Enrollment.user_id == user_id)
    if course_id:
        q = q.filter(Enrollment.course_id == course_id)

    total = q.count()
    rows = (
        q.order_by(Enrollment.enrolled_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": e.id,
            "enrolled_at": e.enrolled_at.isoformat() if e.enrolled_at else None,
            "user": {"id": u.id, "email": u.email, "name": u.name},
            "course": {"id": c.id, "title": c.title},
        }
        for (e, u, c) in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
