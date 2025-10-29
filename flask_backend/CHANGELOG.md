# Changelog

## 0.1.0 - Initial backend scaffolding
- Flask app factory with SQLAlchemy and Alembic
- Core models: users, courses, lessons, enrollments, chat_messages, whiteboard_sessions, whiteboard_events, payments, recommendations_cache
- Migrations initialized and initial migration added
- Diagnostics endpoints: health, status, version, uptime, memory, metrics, proc, cpu, routes, time, echo, ws-help
- Read-only endpoints: users, courses, lessons (by course), enrollments (by user), payments (by user), recommendations (by user)
- OpenAPI JSON served at /openapi.json with extra paths merged
- Seed and helper scripts for dev workflows (export/import, create user, seed augment)
- Makefile targets for common tasks; added pytest smoke tests
