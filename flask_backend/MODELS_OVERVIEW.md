# Models Overview

Core entities:
- users (User)
  - id, email (unique), name, password_hash, role, created_at
  - relationships: enrollments, messages, payments, recommendations_cache (via FK)
- courses (Course)
  - id, title, description, created_at
  - relationships: lessons, enrollments, messages, payments, whiteboard_sessions
- lessons (Lesson)
  - id, course_id -> courses.id, title, content, video_url, created_at
- enrollments (Enrollment)
  - id, user_id -> users.id, course_id -> courses.id, enrolled_at
  - unique: (user_id, course_id)
- chat_messages (ChatMessage)
  - id, course_id, user_id (nullable), content, created_at
- whiteboard_sessions (WhiteboardSession)
  - id, course_id, lesson_id (nullable), status, created_at
- whiteboard_events (WhiteboardEvent)
  - id, session_id -> whiteboard_sessions.id, user_id (nullable), type, payload (JSON), created_at
- payments (Payment)
  - id, user_id, course_id, amount, currency, status, provider, reference, created_at
- recommendations_cache (RecommendationsCache)
  - id, user_id, data (JSON), generated_at, expires_at

Migrations:
- Alembic managed; initial migration creates all tables.
- See migrations/versions/0001_initial.py

Seeding:
- seed.py inserts sample users, one course with lessons, an enrollment, a payment, and a recommendations cache entry.
