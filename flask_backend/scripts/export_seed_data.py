#!/usr/bin/env python
"""
Export key data (users, courses, lessons) to JSON for fixtures/debugging.
"""
import json
from pathlib import Path
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.db import db
    from app.models import User, Course, Lesson

    app = create_app()
    out = {
        "users": [],
        "courses": [],
        "lessons": []
    }
    with app.app_context():
        for u in User.query.order_by(User.id.asc()).all():
            out["users"].append({"id": u.id, "email": u.email, "name": u.name, "role": u.role})
        for c in Course.query.order_by(Course.id.asc()).all():
            out["courses"].append({"id": c.id, "title": c.title, "description": c.description})
        for l in Lesson.query.order_by(Lesson.id.asc()).all():
            out["lessons"].append({"id": l.id, "course_id": l.course_id, "title": l.title, "video_url": l.video_url})
    target = Path(__file__).resolve().parent / "seed_export.json"
    target.write_text(json.dumps(out, indent=2))
    print(f"Wrote {target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
