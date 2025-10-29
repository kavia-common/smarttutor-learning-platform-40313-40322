"""
Flask-SocketIO namespaces for chat and whiteboard.

Namespaces:
- /chat: join room 'course-{course_id}', events: join_room, message
- /whiteboard: join room 'session-{session_id}', events: join_room, draw_event
"""
from __future__ import annotations

from typing import Any, Dict

from flask_socketio import Namespace, emit, join_room


class ChatNamespace(Namespace):
    namespace = "/chat"

    def on_join_room(self, data: Dict[str, Any]):
        course_id = data.get("course_id")
        if not isinstance(course_id, int):
            emit("error", {"error": "course_id must be int"})
            return
        room = f"course-{course_id}"
        join_room(room)
        emit("joined", {"room": room})

    def on_message(self, data: Dict[str, Any]):
        course_id = data.get("course_id")
        content = data.get("content")
        if not isinstance(course_id, int) or not isinstance(content, str):
            emit("error", {"error": "invalid payload"})
            return
        room = f"course-{course_id}"
        emit("message", {"course_id": course_id, "content": content}, to=room)


class WhiteboardNamespace(Namespace):
    namespace = "/whiteboard"

    def on_join_room(self, data: Dict[str, Any]):
        session_id = data.get("session_id")
        if not isinstance(session_id, int):
            emit("error", {"error": "session_id must be int"})
            return
        room = f"session-{session_id}"
        join_room(room)
        emit("joined", {"room": room})

    def on_draw_event(self, data: Dict[str, Any]):
        session_id = data.get("session_id")
        event = data.get("event")
        if not isinstance(session_id, int) or not isinstance(event, dict):
            emit("error", {"error": "invalid payload"})
            return
        room = f"session-{session_id}"
        emit("draw_event", {"session_id": session_id, "event": event}, to=room)
