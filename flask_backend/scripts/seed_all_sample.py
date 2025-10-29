#!/usr/bin/env python
"""
Generate a comprehensive set of sample data for local development:
- Users: alice (student), bob (tutor)
- Courses: Algebra Basics, Calculus I
- Lessons for each course
- Enrollments for alice
- One payment record for alice
- Recommendation cache for alice

Usage:
  python scripts/seed_all_sample.py
"""
from datetime import datetime, timedelta
from app import create_app
from app.db import db
from app.models import User, Course, Lesson, Enrollment, Payment, RecommendationsCache

def main() -> int:
    app = create_app()
    with app.app_context():
        # Users
        alice = db.session.query(User).filter_by(email="alice@example.com").first()
        if not alice:
            alice = User(email="alice@example.com", name="Alice", role="student", password_hash="dev")
            db.session.add(alice)
            db.session.flush()
        bob = db.session.query(User).filter_by(email="bob@example.com").first()
        if not bob:
            bob = User(email="bob@example.com", name="Bob", role="tutor", password_hash="dev")
            db.session.add(bob)
            db.session.flush()

        # Courses
        algebra = db.session.query(Course).filter_by(title="Algebra Basics").first()
        if not algebra:
            algebra = Course(title="Algebra Basics", description="Fundamentals of algebra.")
            db.session.add(algebra)
            db.session.flush()

        calculus = db.session.query(Course).filter_by(title="Calculus I").first()
        if not calculus:
            calculus = Course(title="Calculus I", description="Introduction to limits, derivatives, integrals.")
            db.session.add(calculus)
            db.session.flush()

        # Lessons
        if not db.session.query(Lesson).filter_by(course_id=algebra.id).first():
            db.session.add_all([
                Lesson(course_id=algebra.id, title="Variables and Expressions", content="Intro"),
                Lesson(course_id=algebra.id, title="Linear Equations", content="Equations"),
            ])
        if not db.session.query(Lesson).filter_by(course_id=calculus.id).first():
            db.session.add_all([
                Lesson(course_id=calculus.id, title="Limits", content="Limits intro"),
                Lesson(course_id=calculus.id, title="Derivatives", content="Derivatives intro"),
            ])

        # Enrollments (Alice)
        if not db.session.query(Enrollment).filter_by(user_id=alice.id, course_id=algebra.id).first():
            db.session.add(Enrollment(user_id=alice.id, course_id=algebra.id))
        if not db.session.query(Enrollment).filter_by(user_id=alice.id, course_id=calculus.id).first():
            db.session.add(Enrollment(user_id=alice.id, course_id=calculus.id))

        # Payment for Algebra
        if not db.session.query(Payment).filter_by(user_id=alice.id, course_id=algebra.id).first():
            db.session.add(Payment(user_id=alice.id, course_id=algebra.id, amount=49.99, currency="USD", status="succeeded", provider="stripe"))

        # Recommendations cache
        if not db.session.query(RecommendationsCache).filter_by(user_id=alice.id).first():
            db.session.add(RecommendationsCache(
                user_id=alice.id,
                data={"recommended": ["Calculus I", "Linear Algebra Essentials"]},
                generated_at=datetime.utcnow(),
                expires_at=datetime.utcnow() + timedelta(days=2),
            ))

        db.session.commit()
        print("Seeded sample data.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
