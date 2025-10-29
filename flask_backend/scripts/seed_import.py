#!/usr/bin/env python
"""
Import seed data from JSON to database.
Usage: python scripts/seed_import.py input.json
"""
import json
import sys
from app import create_app
from app.db import db
from app.models import User, Course, Lesson

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/seed_import.py input.json")
        return 2
    inp = sys.argv[1]
    app = create_app()
    with app.app_context():
        data = json.loads(open(inp, "r", encoding="utf-8").read())
        for u in data.get("users", []):
            if not db.session.query(User).filter_by(email=u["email"]).first():
                db.session.add(User(email=u["email"], name=u.get("name") or u["email"], role=u.get("role","student"), password_hash="imported"))
        db.session.flush()

        course_map = {}
        for c in data.get("courses", []):
            course = db.session.query(Course).filter_by(title=c["title"]).first()
            if not course:
                course = Course(title=c["title"], description=c.get("description"))
                db.session.add(course)
                db.session.flush()
            course_map[c["id"]] = course.id

        for l in data.get("lessons", []):
            cid = course_map.get(l["course_id"])
            if not cid:
                continue
            if not db.session.query(Lesson).filter_by(course_id=cid, title=l["title"]).first():
                db.session.add(Lesson(course_id=cid, title=l["title"], video_url=l.get("video_url")))
        db.session.commit()
        print("Seed import completed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
