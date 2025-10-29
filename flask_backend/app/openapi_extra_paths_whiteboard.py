# PUBLIC_INTERFACE
def get_extra_paths_whiteboard() -> dict:
    """Extra OpenAPI paths for whiteboard sessions and events."""
    return {
        "/api/whiteboard/sessions": {
            "get": {
                "summary": "List whiteboard sessions",
                "tags": ["whiteboard"],
                "parameters": [
                    {"name": "course_id", "in": "query", "required": False, "schema": {"type": "integer"}}
                ],
                "responses": {"200": {"description": "List of sessions"}}
            }
        },
        "/api/whiteboard/sessions/{session_id}/events": {
            "get": {
                "summary": "List events for a whiteboard session",
                "tags": ["whiteboard"],
                "parameters": [
                    {"name": "session_id", "in": "path", "required": True, "schema": {"type": "integer"}}
                ],
                "responses": {"200": {"description": "List of events"}}
            }
        }
    }
