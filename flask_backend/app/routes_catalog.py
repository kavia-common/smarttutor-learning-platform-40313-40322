from flask import Blueprint, request, jsonify

catalog_bp = Blueprint("catalog", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@catalog_bp.get("/courses")
def list_courses():
    """
    summary: List courses
    description: Returns a paginated list of courses (placeholder data for now).
    responses:
      200:
        description: List of courses with pagination
    """
    try:
        page = max(int(request.args.get("page", "1")), 1)
        per_page = min(max(int(request.args.get("per_page", "10")), 1), 50)
    except Exception:
        page, per_page = 1, 10
    total = 25
    items = []
    start = (page - 1) * per_page + 1
    end = min(start + per_page - 1, total)
    for i in range(start, end + 1):
        items.append({"id": i, "title": f"Course {i}", "description": "Learn effectively with SmartTutor."})
    return jsonify({"items": items, "page": page, "per_page": per_page, "total": total})

# PUBLIC_INTERFACE
@catalog_bp.get("/courses/<int:course_id>")
def get_course(course_id: int):
    """
    summary: Get course detail
    description: Returns course detail (placeholder).
    responses:
      200:
        description: Course detail
    """
    return jsonify({"id": course_id, "title": f"Course {course_id}", "description": "Course detail."})

# PUBLIC_INTERFACE
@catalog_bp.get("/courses/<int:course_id>/lessons")
def list_lessons(course_id: int):
    """
    summary: List lessons for a course
    description: Returns a list of lessons (placeholder).
    responses:
      200:
        description: Lessons list
    """
    lessons = [{"id": i, "course_id": course_id, "title": f"Lesson {i}", "video_url": None} for i in range(1, 4)]
    return jsonify({"items": lessons})
