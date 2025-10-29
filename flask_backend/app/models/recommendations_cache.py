from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class RecommendationsCache(db.Model):
    """Cache of AI recommendations for a user with TTL semantics."""
    __tablename__ = "recommendations_cache"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # arbitrary recommendations payload
    generated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    user = relationship("User")

    def __repr__(self) -> str:
        return f"<RecommendationsCache user={self.user_id} at={self.generated_at}>"
