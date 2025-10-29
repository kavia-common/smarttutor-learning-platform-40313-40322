"""
Catalog blueprint to list courses, lessons, and search courses.
"""
from __future__ import annotations

from flask import Blueprint, jsonify, request
from sqlalchemy import select
from ..db import db
from ..models import Course, Lesson

catalog_bp = Blueprint("catalog", __name__, url_prefix="/catalog")


# PUBLIC_INTERFACE
@catalog_bp.get("/courses")
def list_courses():
    """
    List all courses.

    Returns:
      200 OK with an array of course objects.
    """
    courses = db.session.execute(select(Course)).scalars().all()
    return jsonify(
        [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "price_cents": c.price_cents,
                "created_by_id": c.created_by_id,
            }
            for c in courses
        ]
    )


# PUBLIC_INTERFACE
@catalog_bp.get("/courses/<int:course_id>/lessons")
def list_lessons(course_id: int):
    """
    List lessons for a specific course.

    Path params:
      - course_id: integer

    Returns:
      200 OK with an array of lesson objects.
    """
    lessons = db.session.execute(select(Lesson).where(Lesson.course_id == course_id)).scalars().all()
    return jsonify(
        [
            {
                "id": l.id,
                "course_id": l.course_id,
                "title": l.title,
                "content_url": l.content_url,
                "order_index": l.order_index,
            }
            for l in lessons
        ]
    )


# PUBLIC_INTERFACE
@catalog_bp.get("/search")
def search_courses():
    """
    Search courses by title substring.

    Query params:
      - q: search string

    Returns:
      200 OK with matching courses.
    """
    q = (request.args.get("q") or "").strip().lower()
    stmt = select(Course)
    if q:
        stmt = stmt.where(Course.title.ilike(f"%{q}%"))
    courses = db.session.execute(stmt).scalars().all()
    return jsonify(
        [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "price_cents": c.price_cents,
                "created_by_id": c.created_by_id,
            }
            for c in courses
        ]
    )
