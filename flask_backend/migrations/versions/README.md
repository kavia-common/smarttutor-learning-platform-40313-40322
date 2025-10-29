Initial migration files live in this directory.

Included:
- 0001_initial.py – Creates base tables:
  users, courses, lessons, enrollments, chat_messages,
  whiteboard_sessions, whiteboard_events, payments, recommendations_cache.

Generate new migrations:
  alembic revision --autogenerate -m "your message"
Apply:
  alembic upgrade head
