"""
WhiteboardSession model representing a collaborative whiteboard timeline per course or lesson.
"""
from __future__ import annotations

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class WhiteboardSession(db.Model):
    """Represents a whiteboard session (e.g., per live session or per lesson)."""

    __tablename__ = "whiteboard_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, default="Session")

    created_by_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    course = relationship("Course", backref="whiteboard_sessions")
    # created_by optional relationship omitted for brevity

    def __repr__(self) -> str:
        return f"<WhiteboardSession id={self.id} course_id={self.course_id}>"
