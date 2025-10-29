from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class WhiteboardEvent(db.Model):
    """Events applied to a whiteboard session (draw, erase, clear, etc.)."""
    __tablename__ = "whiteboard_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("whiteboard_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    type: Mapped[str] = mapped_column(Text, nullable=False)  # e.g. "draw", "erase", "clear"
    payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # arbitrary JSON payload
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    session = relationship("WhiteboardSession", back_populates="events")

    def __repr__(self) -> str:
        return f"<WhiteboardEvent {self.id} session={self.session_id} type={self.type}>"
