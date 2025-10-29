from flask import Blueprint

docs_bp = Blueprint("docs", __name__, url_prefix="/docs")

# PUBLIC_INTERFACE
@docs_bp.get("/ws")
def websocket_usage():
    """Describe WebSocket usage for SmartTutor (documentation-only stub).

    Returns:
        dict: Usage notes describing future WebSocket endpoints.
    """
    return {
        "note": "WebSocket endpoints are planned but not yet implemented.",
        "endpoints": [
            {
                "path": "/ws/chat/{course_id}",
                "summary": "Real-time chat stream for a course",
                "protocol": "ws",
                "messages": [
                    {"type": "chat_message", "payload": {"text": "string"}}
                ],
            },
            {
                "path": "/ws/whiteboard/{session_id}",
                "summary": "Collaborative whiteboard events",
                "protocol": "ws",
                "messages": [
                    {"type": "draw", "payload": {"x": "number", "y": "number", "color": "string"}},
                    {"type": "erase", "payload": {"x": "number", "y": "number", "radius": "number"}},
                    {"type": "clear", "payload": {}},
                ],
            },
        ],
        "client_note": "Use VITE_WS_BASE_URL from the frontend .env to build the WebSocket URL."
    }
