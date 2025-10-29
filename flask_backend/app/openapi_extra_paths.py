def get_extra_paths() -> dict:
    """Return extra OpenAPI paths merged by openapi_register if used."""
    return {
        "/api/proc": {
            "get": {
                "summary": "Process diagnostics",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "PID and thread count"}
                }
            }
        },
        "/api/cpu": {
            "get": {
                "summary": "CPU diagnostics",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "CPU count and load averages"}
                }
            }
        },
        "/api/time": {
            "get": {
                "summary": "Server time (UTC)",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "Current server time"}
                }
            }
        },
        "/api/echo": {
            "get": {
                "summary": "Echo request (GET)",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "Echo payload"}
                }
            },
            "post": {
                "summary": "Echo request (POST)",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "Echo payload"}
                }
            }
        },
        "/api/ws-help": {
            "get": {
                "summary": "WebSocket usage help (placeholder)",
                "tags": ["system"],
                "responses": {
                    "200": {"description": "WS help"}
                }
            }
        },
        "/api/courses": {
            "get": {
                "summary": "List courses (basic read-only)",
                "tags": ["courses"],
                "parameters": [
                    {"name": "page", "in": "query", "schema": {"type": "integer"}, "required": False},
                    {"name": "size", "in": "query", "schema": {"type": "integer"}, "required": False}
                ],
                "responses": {
                    "200": {"description": "Paginated courses list"}
                }
            }
        }
    }
