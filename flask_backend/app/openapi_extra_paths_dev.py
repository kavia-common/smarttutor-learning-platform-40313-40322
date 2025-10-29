def get_extra_paths_dev() -> dict:
    """Extra OpenAPI paths for development helper endpoints."""
    return {
        "/api/dev/enroll": {
            "post": {
                "summary": "Create enrollment (development only)",
                "tags": ["system"],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "user_id": {"type": "integer"},
                                    "course_id": {"type": "integer"}
                                },
                                "required": ["user_id", "course_id"]
                            }
                        }
                    }
                },
                "responses": {"200": {"description": "Enrollment creation result"}}
            }
        }
    }
