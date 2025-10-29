WebSocket Usage Notes (Planned)

SmartTutor will expose WebSocket endpoints for:
- Realtime chat (course room)
- Whiteboard collaborative events (session room)

Docs integration:
- Add explicit WebSocket route registration and tags in OpenAPI builder
- Provide an HTTP docs endpoint summarizing WS usage and connection URLs

Suggested endpoints (to be implemented later):
- ws://<host>:8000/ws/chat?course_id=<id>&token=...
- ws://<host>:8000/ws/whiteboard?session_id=<id>&token=...

See also:
- /openapi.json – REST docs
- /api/diag/routes – list of current HTTP routes
