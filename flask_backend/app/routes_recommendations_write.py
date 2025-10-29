from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request
from .db import db
from .models import RecommendationsCache, User

recs_write_bp = Blueprint("recommendations_write", __name__, url_prefix="/api/recommendations")

# PUBLIC_INTERFACE
@recs_write_bp.post("/compute")
def compute_recommendations():
    """Compute and store recommendations for a user (development stub).

    Body JSON:
      - user_id: int
      - force: bool (optional) recompute regardless of existing cache

    Returns:
      200 with cache entry.
    """
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    force = bool(data.get("force", False))
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    if not User.query.get(user_id):
        return jsonify({"error": f"user_id {user_id} not found"}), 404

    # Stub: compute dummy recommendations
    now = datetime.utcnow()
    payload = {
        "recommended": [
            "Algebra Basics",
            "Calculus I",
            "Linear Algebra Essentials"
        ],
        "generated": now.isoformat() + "Z"
    }

    rec = RecommendationsCache.query.filter_by(user_id=user_id).first()
    if rec and not force:
        # Update timestamps lightly
        rec.generated_at = now
        rec.expires_at = now + timedelta(days=1)
        db.session.commit()
    else:
        if not rec:
            rec = RecommendationsCache(user_id=user_id, data=payload, generated_at=now, expires_at=now + timedelta(days=1))
            db.session.add(rec)
        else:
            rec.data = payload
            rec.generated_at = now
            rec.expires_at = now + timedelta(days=1)
        db.session.commit()

    return jsonify({
        "id": rec.id,
        "user_id": rec.user_id,
        "data": rec.data,
        "generated_at": rec.generated_at.isoformat() if rec.generated_at else None,
        "expires_at": rec.expires_at.isoformat() if rec.expires_at else None
    }), 200
