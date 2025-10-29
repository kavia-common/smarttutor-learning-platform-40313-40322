from __future__ import annotations

from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base


class WhiteboardSession(Base):
    """Represents a whiteboard session tied to a course/lesson."""

    __tablename__ = "whiteboard_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int | None] = mapped_column(ForeignKey("courses.id"), index=True)
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id"), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    events: Mapped[list["WhiteboardEvent"]] = relationship(
        "WhiteboardEvent", back_populates="session", cascade="all,delete-orphan"
    )
