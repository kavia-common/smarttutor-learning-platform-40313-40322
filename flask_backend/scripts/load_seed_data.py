#!/usr/bin/env python
"""
Load seed data from scripts/seed_export.json (created by export_seed_data.py).
"""
import json
from pathlib import Path
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.db import db
    from app.models import User, Course, Lesson

    data_path = Path(__file__).resolve().parent / "seed_export.json"
    if not data_path.exists():
        print(f"Seed file not found: {data_path}")
        return 1

    data = json.loads(data_path.read_text())
    app = create_app()
    with app.app_context():
        # Insert users (skip existing emails)
        existing_emails = {u.email for u in User.query.all()}
        for u in data.get("users", []):
            if u["email"] in existing_emails:
                continue
            user = User(email=u["email"], name=u.get("name") or u["email"].split("@")[0], password_hash="imported", role=u.get("role") or "student")
            db.session.add(user)
        db.session.flush()

        # Insert courses (skip existing titles)
        existing_titles = {c.title for c in Course.query.all()}
        id_map = {}
        for c in data.get("courses", []):
            if c["title"] in existing_titles:
                existing = Course.query.filter_by(title=c["title"]).first()
                id_map[c["id"]] = existing.id
                continue
            course = Course(title=c["title"], description=c.get("description"))
            db.session.add(course)
            db.session.flush()
            id_map[c["id"]] = course.id

        # Insert lessons
        for l in data.get("lessons", []):
            course_id = id_map.get(l["course_id"])
            if not course_id:
                continue
            lesson = Lesson(course_id=course_id, title=l["title"], video_url=l.get("video_url"))
            db.session.add(lesson)

        db.session.commit()
        print("Seed data loaded.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
