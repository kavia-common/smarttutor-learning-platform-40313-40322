# Note: Before running this script, ensure flask_backend/.env exists with DATABASE_URL and JWT_SECRET.
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app import create_app
from app.db import db
from app.models import User, Course, Lesson, Enrollment, Payment, RecommendationsCache

def main():
    """Seed initial data for development."""
    load_dotenv()
    app = create_app()
    with app.app_context():
        # Create some sample users
        alice = User(email="alice@example.com", name="Alice", password_hash="hash_alice", role="student")
        bob = User(email="bob@example.com", name="Bob", password_hash="hash_bob", role="tutor")
        db.session.add_all([alice, bob])
        db.session.flush()

        # Create sample course with lessons
        course = Course(title="Algebra Basics", description="Learn the fundamentals of algebra.")
        db.session.add(course)
        db.session.flush()

        lessons = [
            Lesson(course_id=course.id, title="Variables and Expressions", content="Intro content"),
            Lesson(course_id=course.id, title="Linear Equations", content="More content"),
        ]
        db.session.add_all(lessons)

        # Add a second course
        course2 = Course(title="Calculus I", description="Limits, derivatives, and integrals.")
        db.session.add(course2)
        db.session.flush()
        lessons2 = [
            Lesson(course_id=course2.id, title="Limits", content="Intro to limits"),
            Lesson(course_id=course2.id, title="Derivatives", content="Intro to derivatives"),
        ]
        db.session.add_all(lessons2)

        # Enroll Alice
        enroll = Enrollment(user_id=alice.id, course_id=course.id)
        db.session.add(enroll)

        # Payment record
        payment = Payment(user_id=alice.id, course_id=course.id, amount=49.99, currency="USD", status="succeeded", provider="stripe")
        db.session.add(payment)

        # Recommendation cache
        rec = RecommendationsCache(
            user_id=alice.id,
            data={"recommended": ["Calculus I", "Linear Algebra Essentials"]},
            generated_at=datetime.utcnow(),
            expires_at=datetime.utcnow() + timedelta(days=1),
        )
        db.session.add(rec)

        # Chat message sample
        from app.models import ChatMessage, WhiteboardSession, WhiteboardEvent
        chat1 = ChatMessage(course_id=course.id, user_id=alice.id, content="Hello, I love this course!")
        chat2 = ChatMessage(course_id=course.id, user_id=bob.id, content="Welcome Alice, let's start with variables.")
        db.session.add_all([chat1, chat2])

        # Whiteboard session + events
        session = WhiteboardSession(course_id=course.id, lesson_id=None, status="active")
        db.session.add(session)
        db.session.flush()
        evt1 = WhiteboardEvent(session_id=session.id, user_id=bob.id, type="draw", payload={"x": 10, "y": 12, "color": "#2563EB"})
        evt2 = WhiteboardEvent(session_id=session.id, user_id=alice.id, type="draw", payload={"x": 30, "y": 40, "color": "#F59E0B"})
        db.session.add_all([evt1, evt2])

        db.session.commit()
        print("Seed data inserted.")

if __name__ == "__main__":
    # Ensure DATABASE_URL and JWT_SECRET exist
    if not os.getenv("DATABASE_URL"):
        print("ERROR: DATABASE_URL not set. Create .env from .env.example and set your variables.")
        raise SystemExit(1)
    if not os.getenv("JWT_SECRET"):
        print("ERROR: JWT_SECRET not set. Create .env from .env.example and set your variables.")
        raise SystemExit(1)
    main()
