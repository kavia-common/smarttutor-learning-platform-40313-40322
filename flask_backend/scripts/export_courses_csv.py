#!/usr/bin/env python
"""
Export courses and lessons to CSV files for quick inspection.
"""
import csv
from pathlib import Path
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.models import Course, Lesson

    app = create_app()
    out_dir = Path(__file__).resolve().parent
    courses_csv = out_dir / "courses.csv"
    lessons_csv = out_dir / "lessons.csv"

    with app.app_context():
        # Courses
        with courses_csv.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "title", "description", "created_at"])
            for c in Course.query.order_by(Course.id.asc()).all():
                writer.writerow([c.id, c.title, (c.description or "").replace("\n", " "), c.created_at])

        # Lessons
        with lessons_csv.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "course_id", "title", "video_url", "created_at"])
            for l in Lesson.query.order_by(Lesson.id.asc()).all():
                writer.writerow([l.id, l.course_id, l.title, l.video_url or "", l.created_at])

    print(f"Wrote {courses_csv} and {lessons_csv}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
