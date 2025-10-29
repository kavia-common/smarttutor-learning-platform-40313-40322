from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from .db import db
from .models import Payment, User, Course
from .auth_decorators import login_required
from decimal import Decimal

payments_write_bp = Blueprint("payments_write", __name__, url_prefix="/api/payments")

# PUBLIC_INTERFACE
@payments_write_bp.post("/")
@login_required
def create_payment():
    """Create a payment record (development stub; does not contact an external provider).

    Body JSON:
      - user_id: int
      - course_id: int
      - amount: number
      - currency: string (default 'USD')
      - provider: optional string
      - reference: optional string

    Returns:
      201 with created payment record.
    """
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    course_id = data.get("course_id")
    amount = data.get("amount")
    currency = (data.get("currency") or "USD").upper()
    provider = data.get("provider") or "stub"
    reference = data.get("reference")

    if not user_id or not course_id or amount is None:
        return jsonify({"error": "user_id, course_id, and amount are required"}), 400

    # Validate references exist
    if not User.query.get(user_id):
        return jsonify({"error": f"user_id {user_id} not found"}), 404
    if not Course.query.get(course_id):
        return jsonify({"error": f"course_id {course_id} not found"}), 404

    try:
        amt = Decimal(str(amount))
    except Exception:
        return jsonify({"error": "amount must be a number"}), 400

    p = Payment(
        user_id=user_id,
        course_id=course_id,
        amount=amt,
        currency=currency,
        status="succeeded",  # dev default
        provider=provider,
        reference=reference,
    )
    try:
        db.session.add(p)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "failed to persist payment"}), 400

    return jsonify({
        "id": p.id,
        "user_id": p.user_id,
        "course_id": p.course_id,
        "amount": float(p.amount) if p.amount is not None else None,
        "currency": p.currency,
        "status": p.status,
        "provider": p.provider,
        "reference": p.reference,
        "created_at": p.created_at.isoformat() if p.created_at else None,
    }), 201
