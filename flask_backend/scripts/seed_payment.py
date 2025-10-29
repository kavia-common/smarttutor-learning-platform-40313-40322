#!/usr/bin/env python
"""
Create a demo payment for a given user and course.
Usage: python scripts/seed_payment.py user_id course_id [amount] [currency]
"""
import sys
from decimal import Decimal
from app import create_app
from app.db import db
from app.models import User, Course, Payment

def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/seed_payment.py user_id course_id [amount] [currency]")
        return 2
    user_id = int(sys.argv[1])
    course_id = int(sys.argv[2])
    amount = Decimal(sys.argv[3]) if len(sys.argv) > 3 else Decimal("49.99")
    currency = sys.argv[4] if len(sys.argv) > 4 else "USD"

    app = create_app()
    with app.app_context():
        u = db.session.get(User, user_id)
        c = db.session.get(Course, course_id)
        if not u or not c:
            print("User or course not found")
            return 1
        pay = Payment(user_id=u.id, course_id=c.id, amount=amount, currency=currency, status="succeeded", provider="stripe")
        db.session.add(pay)
        db.session.commit()
        print(f"Created payment id={pay.id} user={u.id} course={c.id} amount={amount} {currency}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
