"""
Lesson model.
"""
from __future__ import annotations

from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Lesson(db.Model):
    """Represents a lesson within a course."""

    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    order_index: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    course = relationship("Course", backref="lessons")

    def __repr__(self) -> str:
        return f"<Lesson id={self.id} course_id={self.course_id} title={self.title}>"
