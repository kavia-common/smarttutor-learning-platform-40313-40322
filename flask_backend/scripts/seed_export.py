#!/usr/bin/env python
"""
Export minimal seed data (users, courses, lessons) to JSON.
Usage: python scripts/seed_export.py [output.json]
"""
import json
import sys
from app import create_app
from app.db import db
from app.models import User, Course, Lesson

def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "seed_export.json"
    app = create_app()
    with app.app_context():
        users = [
            {"id": u.id, "email": u.email, "name": u.name, "role": u.role}
            for u in db.session.query(User).all()
        ]
        courses = [
            {"id": c.id, "title": c.title, "description": c.description}
            for c in db.session.query(Course).all()
        ]
        lessons = [
            {"id": l.id, "course_id": l.course_id, "title": l.title, "video_url": l.video_url}
            for l in db.session.query(Lesson).all()
        ]
        payload = {"users": users, "courses": courses, "lessons": lessons}
        with open(out, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
