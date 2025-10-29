"""
Enrollments blueprint to create and list enrollments for the current user.
"""
from __future__ import annotations

from flask import Blueprint, jsonify, request
from sqlalchemy import select

from ..db import db
from ..models import Enrollment, Course
from .auth import _current_user

enroll_bp = Blueprint("enrollments", __name__, url_prefix="/enrollments")


# PUBLIC_INTERFACE
@enroll_bp.get("")
def list_my_enrollments():
    """
    List enrollments for the current user.

    Headers:
      - Authorization: Bearer user-{id}

    Returns:
      200 OK with an array of enrollments including course info.
    """
    user = _current_user()
    if not user:
        return jsonify({"error": "unauthorized"}), 401

    enrollments = db.session.execute(select(Enrollment).where(Enrollment.user_id == user.id)).scalars().all()
    result = []
    for e in enrollments:
        result.append(
            {
                "id": e.id,
                "course_id": e.course_id,
                "status": e.status,
                "course": {
                    "id": e.course.id,
                    "title": e.course.title,
                    "description": e.course.description,
                    "price_cents": e.course.price_cents,
                },
            }
        )
    return jsonify(result)


# PUBLIC_INTERFACE
@enroll_bp.post("")
def create_enrollment():
    """
    Create an enrollment for the current user in a course.

    Request JSON:
      - course_id: integer

    Returns:
      201 Created with enrollment data, or 409 if already enrolled.
    """
    user = _current_user()
    if not user:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    course_id = data.get("course_id")
    if not isinstance(course_id, int):
        return jsonify({"error": "course_id is required"}), 400

    course = db.session.get(Course, course_id)
    if not course:
        return jsonify({"error": "course not found"}), 404

    existing = db.session.execute(
        select(Enrollment).where(Enrollment.user_id == user.id, Enrollment.course_id == course_id)
    ).scalar_one_or_none()
    if existing:
        return jsonify({"error": "already enrolled"}), 409

    e = Enrollment(user_id=user.id, course_id=course_id, status="active")
    db.session.add(e)
    db.session.commit()
    return (
        jsonify(
            {
                "id": e.id,
                "course_id": e.course_id,
                "status": e.status,
            }
        ),
        201,
    )
