from flask import Blueprint, jsonify, request
from app.db import db
from app.models import RecommendationsCache, User

recommendations_bp = Blueprint("recommendations", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@recommendations_bp.get("/recommendations/cache")
def list_recommendations_cache():
    """List recommendation cache entries (read-only, dev/diagnostics).

    Query params:
    - user_id: optional filter by user
    - limit: max items (default 100, max 500)
    - offset: offset for pagination (default 0)
    """
    user_id = request.args.get("user_id", type=int)
    limit = min(max(request.args.get("limit", type=int) or 100, 1), 500)
    offset = max(request.args.get("offset", type=int) or 0, 0)

    q = (
        db.session.query(RecommendationsCache, User)
        .join(User, RecommendationsCache.user_id == User.id)
    )
    if user_id:
        q = q.filter(RecommendationsCache.user_id == user_id)

    total = q.count()
    rows = (
        q.order_by(RecommendationsCache.generated_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    data = [
        {
            "id": rc.id,
            "user": {"id": u.id, "email": u.email, "name": u.name},
            "data": rc.data,
            "generated_at": rc.generated_at.isoformat() if rc.generated_at else None,
            "expires_at": rc.expires_at.isoformat() if rc.expires_at else None,
        }
        for (rc, u) in rows
    ]
    return jsonify({"total": total, "items": data, "limit": limit, "offset": offset})
