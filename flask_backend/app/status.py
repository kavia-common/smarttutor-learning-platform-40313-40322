from flask import Blueprint
from .db import db
from .models import User, Course, Lesson, Enrollment, ChatMessage, WhiteboardSession, WhiteboardEvent, Payment, RecommendationsCache

status_bp = Blueprint("status", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@status_bp.get("/status")
def status():
    """Return basic entity counts for quick diagnostics.

    Returns:
        dict: counts of key tables.
    """
    def count(model):
        return db.session.query(model).count()
    return {
        "users": count(User),
        "courses": count(Course),
        "lessons": count(Lesson),
        "enrollments": count(Enrollment),
        "chat_messages": count(ChatMessage),
        "whiteboard_sessions": count(WhiteboardSession),
        "whiteboard_events": count(WhiteboardEvent),
        "payments": count(Payment),
        "recommendations_cache": count(RecommendationsCache),
    }
