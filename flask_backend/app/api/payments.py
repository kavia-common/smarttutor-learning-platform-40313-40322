"""
Payments blueprint to create Stripe payment intents.

Environment:
- STRIPE_SK: Stripe secret key (must be configured in .env)

Note: Webhook signing/secret is intentionally omitted as requested.
"""
from __future__ import annotations

import os
from flask import Blueprint, jsonify, request
from ..models import Course, Payment
from ..db import db

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

try:
    import stripe  # type: ignore
except Exception:  # pragma: no cover
    stripe = None  # Fallback to allow import even if dependency missing


def _require_stripe():
    if stripe is None:
        raise RuntimeError("Stripe SDK is not installed. Please add 'stripe' to requirements.txt and install.")
    sk = os.getenv("STRIPE_SK")
    if not sk:
        raise RuntimeError("STRIPE_SK is not set in environment (.env).")
    stripe.api_key = sk


# PUBLIC_INTERFACE
@payments_bp.post("/intent")
def create_payment_intent():
    """
    Create a Stripe PaymentIntent for the requested course.

    Request JSON:
      - course_id: integer

    Returns:
      200 OK with client_secret and payment record.
    """
    data = request.get_json(silent=True) or {}
    course_id = data.get("course_id")
    if not isinstance(course_id, int):
        return jsonify({"error": "course_id is required"}), 400

    course = db.session.get(Course, course_id)
    if not course:
        return jsonify({"error": "course not found"}), 404

    try:
        _require_stripe()
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

    intent = stripe.PaymentIntent.create(  # type: ignore[attr-defined]
        amount=int(course.price_cents or 0),
        currency="usd",
        automatic_payment_methods={"enabled": True},
        metadata={"course_id": str(course.id)},
    )

    payment = Payment(
        user_id=0,  # could be set from auth in the future
        course_id=course.id,
        amount_cents=course.price_cents,
        currency="usd",
        status="pending",
        provider="stripe",
        provider_payment_id=intent["id"],
    )
    db.session.add(payment)
    db.session.commit()

    return jsonify({"client_secret": intent["client_secret"], "payment_id": payment.id})
