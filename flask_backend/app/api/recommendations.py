"""
Recommendations blueprint providing heuristic-based recommendations.

Heuristics:
- If query param 'q' provided: prefer courses whose titles contain q (case-insensitive)
- Otherwise: recommend cheapest courses first
"""
from __future__ import annotations

from flask import Blueprint, jsonify, request
from sqlalchemy import select, func
from ..db import db
from ..models import Course, Enrollment

reco_bp = Blueprint("recommendations", __name__, url_prefix="/recommendations")


# PUBLIC_INTERFACE
@reco_bp.get("")
def recommend():
    """
    Get heuristic recommendations.

    Query params:
      - q: optional search term

    Returns:
      200 OK with list of recommended courses.
    """
    q = (request.args.get("q") or "").strip().lower()
    stmt = select(Course)
    if q:
        stmt = stmt.where(Course.title.ilike(f"%{q}%"))
    courses = db.session.execute(stmt).scalars().all()

    # If no q, prefer cheapest first; break ties with id
    if not q:
        courses.sort(key=lambda c: (c.price_cents, c.id))

    # Attach a simple popularity score: enrollment count
    enroll_counts = dict(
        db.session.execute(
            select(Enrollment.course_id, func.count(Enrollment.id)).group_by(Enrollment.course_id)
        ).all()
    )

    return jsonify(
        [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "price_cents": c.price_cents,
                "popularity": int(enroll_counts.get(c.id, 0)),
            }
            for c in courses
        ]
    )
