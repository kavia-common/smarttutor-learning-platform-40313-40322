#!/usr/bin/env python
"""
Create an enrollment for a given user and course.
Usage: python scripts/seed_enrollment.py user_id course_id
"""
import sys
from app import create_app
from app.db import db
from app.models import Enrollment, User, Course

def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/seed_enrollment.py user_id course_id")
        return 2
    user_id = int(sys.argv[1])
    course_id = int(sys.argv[2])

    app = create_app()
    with app.app_context():
        u = db.session.get(User, user_id)
        c = db.session.get(Course, course_id)
        if not u or not c:
            print("User or course not found")
            return 1
        exists = db.session.query(Enrollment).filter_by(user_id=u.id, course_id=c.id).first()
        if exists:
            print("Enrollment already exists")
            return 0
        db.session.add(Enrollment(user_id=u.id, course_id=c.id))
        db.session.commit()
        print(f"Created enrollment user={u.id} course={c.id}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
