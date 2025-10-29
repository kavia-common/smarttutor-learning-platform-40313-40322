from flask import Blueprint, jsonify
from app.db import db
from app.models import Payment, Course, User

receipt_bp = Blueprint("payment_receipt", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@receipt_bp.get("/payments/<int:payment_id>")
def get_payment_receipt(payment_id: int):
    """Return a simple payment receipt-like payload for a given payment id (development/testing only)."""
    row = (
        db.session.query(Payment, Course, User)
        .join(Course, Payment.course_id == Course.id)
        .join(User, Payment.user_id == User.id)
        .filter(Payment.id == payment_id)
        .first()
    )
    if not row:
        return jsonify({"error": "not_found"}), 404
    payment, course, user = row
    return jsonify({
        "payment": {
            "id": payment.id,
            "amount": float(payment.amount) if payment.amount is not None else None,
            "currency": payment.currency,
            "status": payment.status,
            "provider": payment.provider,
            "reference": payment.reference,
            "created_at": payment.created_at.isoformat() if payment.created_at else None,
        },
        "course": {"id": course.id, "title": course.title},
        "user": {"id": user.id, "email": user.email, "name": user.name},
    })
