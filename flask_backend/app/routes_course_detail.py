from flask import Blueprint, jsonify
from .models import Course, Lesson

course_detail_bp = Blueprint("course_detail", __name__, url_prefix="/api/course")

# PUBLIC_INTERFACE
@course_detail_bp.get("/<int:course_id>")
def get_course(course_id: int):
    """Get a single course by id including its lessons."""
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "course not found"}), 404
    lessons = Lesson.query.with_entities(Lesson.id, Lesson.title, Lesson.video_url).filter_by(course_id=course_id).order_by(Lesson.id.asc()).all()
    return jsonify({
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "lessons": [{"id": l.id, "title": l.title, "video_url": l.video_url} for l in lessons]
    })
