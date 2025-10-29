from flask import Blueprint, jsonify, request
from .db import db
from .models import ChatMessage, User

chat_bp = Blueprint("chat", __name__, url_prefix="/api/chat")

# PUBLIC_INTERFACE
@chat_bp.get("/messages")
def list_messages():
    """List chat messages, optionally filtered by course_id.

    Query params:
        course_id (int, optional): Filter messages by course.

    Returns:
        list[dict]: Array of messages (id, course_id, user_id, content, created_at, user_name).
    """
    q = db.session.query(
        ChatMessage.id,
        ChatMessage.course_id,
        ChatMessage.user_id,
        ChatMessage.content,
        ChatMessage.created_at,
        User.name.label("user_name"),
    ).outerjoin(User, User.id == ChatMessage.user_id)

    course_id = request.args.get("course_id", type=int)
    if course_id:
        q = q.filter(ChatMessage.course_id == course_id)

    q = q.order_by(ChatMessage.id.asc())
    rows = q.all()

    return jsonify(
        [
            {
                "id": r.id,
                "course_id": r.course_id,
                "user_id": r.user_id,
                "user_name": r.user_name,
                "content": r.content,
                "created_at": r.created_at.isoformat() if r.created_at else None,
            }
            for r in rows
        ]
    )
