from flask import Blueprint, jsonify
from alembic.config import Config
from alembic.script import ScriptDirectory
from .db import db
from .models import (
    User, Course, Lesson, Enrollment, ChatMessage,
    WhiteboardSession, WhiteboardEvent, Payment, RecommendationsCache
)

diagnostics_bp = Blueprint("diagnostics", __name__, url_prefix="/api/diag")

# PUBLIC_INTERFACE
@diagnostics_bp.get("/alembic")
def alembic_info():
    """Return Alembic head info and known model tables."""
    try:
        cfg = Config("alembic.ini")
        script = ScriptDirectory.from_config(cfg)
        head = script.get_current_head()
    except Exception as e:
        head = f"unavailable: {e}"
    tables = [
        User.__tablename__,
        Course.__tablename__,
        Lesson.__tablename__,
        Enrollment.__tablename__,
        ChatMessage.__tablename__,
        WhiteboardSession.__tablename__,
        WhiteboardEvent.__tablename__,
        Payment.__tablename__,
        RecommendationsCache.__tablename__,
    ]
    return jsonify({"alembic_head": head, "tables": tables})
