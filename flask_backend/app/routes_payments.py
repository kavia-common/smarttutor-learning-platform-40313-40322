from flask import Blueprint, jsonify, request
from app.db import db
from app.models import Payment, User, Course

payments_bp = Blueprint("payments", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@payments_bp.get("/payments")
def list_payments():
    """List payments (read-only, dev/diagnostics).

    Query params:
    - user_id: filter by user
    - course_id: filter by course
    - status: filter by status (e.g., succeeded, pending, failed)
    - limit: max items (default 100, max 500)
    - offset: offset for pagination (default 0)
    """
    user_id = request.args.get("user_id", type=int)
    course_id = request.args.get("course_id", type=int)
    status = (request.args.get("status") or "").strip()
    limit = min(max(request.args.get("limit", type=int) or 100, 1), 500)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    q = (
        db.session.query(Payment, User, Course)
        .join(User, Payment.user_id == User.id)
        .join(Course, Payment.course_id == Course.id)
    )
    if user_id:
        q = q.filter(Payment.user_id == user_id)
    if course_id:
        q = q.filter(Payment.course_id == course_id)
    if status:
        q = q.filter(Payment.status == status)

    total = q.count()
    rows = (
        q.order_by(Payment.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": p.id,
            "amount": float(p.amount) if p.amount is not None else None,
            "currency": p.currency,
            "status": p.status,
            "provider": p.provider,
            "reference": p.reference,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "user": {"id": u.id, "email": u.email, "name": u.name},
            "course": {"id": c.id, "title": c.title},
        }
        for (p, u, c) in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
