from flask import Blueprint, jsonify

ws_help_bp = Blueprint("ws_help", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@ws_help_bp.get("/ws-help")
def ws_help():
    """
    summary: WebSocket usage help (placeholder)
    description: Documents planned WebSocket endpoints for chat and whiteboard.
    responses:
      200:
        description: WebSocket usage information
    """
    return jsonify({
        "message": "WebSocket endpoints are planned for chat and whiteboard.",
        "examples": {
            "chat": "ws://localhost:8000/ws/chat?course_id=<id>&token=<jwt>",
            "whiteboard": "ws://localhost:8000/ws/whiteboard?session_id=<id>&token=<jwt>"
        }
    })
