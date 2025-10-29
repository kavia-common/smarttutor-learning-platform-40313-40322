from flask import Blueprint, jsonify
from .models import Lesson, Course

lesson_detail_bp = Blueprint("lesson_detail", __name__, url_prefix="/api/lesson")

# PUBLIC_INTERFACE
@lesson_detail_bp.get("/<int:lesson_id>")
def get_lesson(lesson_id: int):
    """Get a single lesson by id including parent course."""
    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        return jsonify({"error": "lesson not found"}), 404
    course = Course.query.get(lesson.course_id)
    return jsonify({
        "id": lesson.id,
        "title": lesson.title,
        "content": lesson.content,
        "video_url": lesson.video_url,
        "course": {"id": course.id, "title": course.title} if course else None
    })
