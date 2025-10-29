# Whiteboard API (Development)

Endpoints:
- GET /api/whiteboard/sessions
  - Query: course_id (optional)
- GET /api/whiteboard/sessions/{session_id}/events

Examples:
- List sessions:
  curl http://localhost:8000/api/whiteboard/sessions

- List sessions for a course:
  curl "http://localhost:8000/api/whiteboard/sessions?course_id=1"

- List events for a session:
  curl http://localhost:8000/api/whiteboard/sessions/1/events
