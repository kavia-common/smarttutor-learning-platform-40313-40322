def build_openapi() -> dict:
    """
    Build a minimal OpenAPI JSON document describing the currently implemented endpoints.
    Note: This is a static builder for documentation and discoverability.
    """
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "SmartTutor Backend API",
            "description": "REST API for SmartTutor platform",
            "version": "0.1.0",
        },
        "tags": [
            {"name": "system", "description": "System and diagnostics"},
            {"name": "auth", "description": "Authentication and profile"},
            {"name": "courses", "description": "Course catalog APIs"},
            {"name": "lessons", "description": "Lesson endpoints"},
        ],
        "paths": {
            "/health": {
                "get": {
                    "summary": "Health check",
                    "tags": ["system"],
                    "responses": {"200": {"description": "ok"}}
                }
            },
            "/api/status": {
                "get": {
                    "summary": "Backend status",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Name, version, ok flag"}}
                }
            },
            "/api/version": {
                "get": {
                    "summary": "Backend version",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Version info"}}
                }
            },
            "/api/diag/alembic": {
                "get": {
                    "summary": "Alembic head and tables",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Diagnostic info"}}
                }
            },
            "/api/diag/routes": {
                "get": {
                    "summary": "List registered routes",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Array of routes"}}
                }
            },
            "/api/ws-help": {
                "get": {
                    "summary": "WebSocket usage help (placeholder)",
                    "tags": ["system"],
                    "responses": {"200": {"description": "WS help"}}
                }
            },
            "/api/config": {
                "get": {
                    "summary": "Config diagnostics (safe subset)",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Diagnostics payload"}}
                }
            },
            "/api/time": {
                "get": {
                    "summary": "Server time (UTC)",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Current server time"}}
                }
            },
            "/api/uptime": {
                "get": {
                    "summary": "Service uptime since start",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Uptime payload"}}
                }
            },
            "/api/ping": {
                "get": {
                    "summary": "Ping",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Pong"}}
                }
            },
            "/api/memory": {
                "get": {
                    "summary": "Service memory usage",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Memory usage payload"}}
                }
            },
            "/api/versions": {
                "get": {
                    "summary": "Runtime versions",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Python and package availability"}}
                }
            },
            "/api/metrics": {
                "get": {
                    "summary": "In-memory request counters",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Counts by path"}}
                }
            },
            "/api/echo": {
                "get": {
                    "summary": "Echo request info (debug)",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Echo payload"}}
                },
                "post": {
                    "summary": "Echo request info (debug)",
                    "tags": ["system"],
                    "responses": {"200": {"description": "Echo payload"}}
                }
            },
            "/api/auth/register": {
                "post": {
                    "summary": "Register a new user (dev placeholder)",
                    "tags": ["auth"],
                    "responses": {"200": {"description": "Token and user payload"}}
                }
            },
            "/api/auth/login": {
                "post": {
                    "summary": "Login (dev placeholder)",
                    "tags": ["auth"],
                    "responses": {"200": {"description": "Token and user payload"}}
                }
            },
            "/api/auth/profile": {
                "get": {
                    "summary": "Profile (dev placeholder)",
                    "tags": ["auth"],
                    "responses": {"200": {"description": "Profile payload"}}
                }
            },
            "/api/courses": {
                "get": {
                    "summary": "List courses (placeholder)",
                    "tags": ["courses"],
                    "responses": {"200": {"description": "Paginated list"}}
                }
            },
            "/api/courses/{course_id}": {
                "get": {
                    "summary": "Get course (placeholder)",
                    "tags": ["courses"],
                    "responses": {"200": {"description": "Course detail"}}
                }
            },
            "/api/courses/{course_id}/lessons": {
                "get": {
                    "summary": "List lessons (placeholder)",
                    "tags": ["lessons"],
                    "responses": {"200": {"description": "Lessons list"}}
                }
            },
        },
    }
