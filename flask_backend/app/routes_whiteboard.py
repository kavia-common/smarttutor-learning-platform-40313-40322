from flask import Blueprint, jsonify, request
from app.db import db
from app.models import WhiteboardSession, WhiteboardEvent

whiteboard_bp = Blueprint("whiteboard", __name__, url_prefix="/api/whiteboard")

# PUBLIC_INTERFACE
@whiteboard_bp.get("/sessions")
def list_sessions():
    """List whiteboard sessions, optionally filtered by course_id."""
    course_id = request.args.get("course_id", type=int)
    q = db.session.query(WhiteboardSession)
    if course_id:
        q = q.filter(WhiteboardSession.course_id == course_id)
    rows = q.order_by(WhiteboardSession.created_at.desc()).limit(100).all()
    return jsonify([
        {
            "id": s.id,
            "course_id": s.course_id,
            "lesson_id": s.lesson_id,
            "status": s.status,
            "created_at": s.created_at.isoformat() if s.created_at else None,
        }
        for s in rows
    ])

# PUBLIC_INTERFACE
@whiteboard_bp.get("/sessions/<int:session_id>/events")
def list_events(session_id: int):
    """List events for a whiteboard session."""
    rows = (
        db.session.query(WhiteboardEvent)
        .filter(WhiteboardEvent.session_id == session_id)
        .order_by(WhiteboardEvent.created_at.asc())
        .limit(1000)
        .all()
    )
    return jsonify([
        {
            "id": e.id,
            "session_id": e.session_id,
            "user_id": e.user_id,
            "type": e.type,
            "payload": e.payload,
            "created_at": e.created_at.isoformat() if e.created_at else None,
        }
        for e in rows
    ])
