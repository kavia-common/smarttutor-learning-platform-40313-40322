from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class WhiteboardSession(db.Model):
    """A collaborative whiteboard session for a course (optionally tied to a lesson)."""
    __tablename__ = "whiteboard_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id", ondelete="SET NULL"), nullable=True, index=True)
    status: Mapped[str] = mapped_column(String(32), default="active", nullable=False)  # active, archived
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    course = relationship("Course", back_populates="whiteboard_sessions")
    events = relationship("WhiteboardEvent", back_populates="session", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<WhiteboardSession {self.id} course={self.course_id}>"
