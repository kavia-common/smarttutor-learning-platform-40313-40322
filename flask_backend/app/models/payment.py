from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Payment(db.Model):
    """Payments for course purchases."""
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"), nullable=False, index=True)
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(8), nullable=False, default="USD")
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="succeeded")  # pending, succeeded, failed
    provider: Mapped[str] = mapped_column(String(64), nullable=True)  # e.g., stripe
    reference: Mapped[str | None] = mapped_column(String(255), nullable=True)  # provider reference
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="payments")
    course = relationship("Course", back_populates="payments")

    def __repr__(self) -> str:
        return f"<Payment {self.id} user={self.user_id} course={self.course_id} {self.amount} {self.currency}>"
