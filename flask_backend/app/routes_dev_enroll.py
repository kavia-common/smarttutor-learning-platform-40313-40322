from flask import Blueprint, jsonify, request
from app.db import db
from app.models import Enrollment, User, Course

dev_enroll_bp = Blueprint("dev_enroll", __name__, url_prefix="/api/dev")

# PUBLIC_INTERFACE
@dev_enroll_bp.post("/enroll")
def dev_enroll():
    """Create an enrollment for a user and course (development only)."""
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    course_id = data.get("course_id")
    if not user_id or not course_id:
        return jsonify({"error": "user_id and course_id required"}), 400

    user = db.session.get(User, int(user_id))
    course = db.session.get(Course, int(course_id))
    if not user or not course:
        return jsonify({"error": "user_or_course_not_found"}), 404

    # Check existing
    found = db.session.query(Enrollment).filter_by(user_id=user.id, course_id=course.id).first()
    if found:
        return jsonify({"status": "exists", "user_id": user.id, "course_id": course.id})

    enr = Enrollment(user_id=user.id, course_id=course.id)
    db.session.add(enr)
    db.session.commit()
    return jsonify({"status": "created", "user_id": user.id, "course_id": course.id})
