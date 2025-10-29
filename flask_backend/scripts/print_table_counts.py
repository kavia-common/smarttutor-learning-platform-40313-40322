#!/usr/bin/env python
"""
Print table names and row counts for core models.
"""
from app import create_app
from app.db import db
from app.models import (
    User, Course, Lesson, Enrollment, ChatMessage,
    WhiteboardSession, WhiteboardEvent, Payment, RecommendationsCache
)

def count(model):
    return db.session.execute(db.select(db.func.count()).select_from(model)).scalar_one()

def main() -> int:
    app = create_app()
    with app.app_context():
        rows = [
            ("users", count(User)),
            ("courses", count(Course)),
            ("lessons", count(Lesson)),
            ("enrollments", count(Enrollment)),
            ("chat_messages", count(ChatMessage)),
            ("whiteboard_sessions", count(WhiteboardSession)),
            ("whiteboard_events", count(WhiteboardEvent)),
            ("payments", count(Payment)),
            ("recommendations_cache", count(RecommendationsCache)),
        ]
        width = max(len(name) for name, _ in rows)
        for name, c in rows:
            print(f"{name.ljust(width)} : {c}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
