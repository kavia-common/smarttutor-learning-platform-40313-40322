#!/usr/bin/env python
"""
Ping a set of core/dev endpoints and print concise HTTP status results.
"""
import sys
import urllib.request

BASE = "http://localhost:8000"

PATHS = [
    "/",
    "/health",
    "/openapi.json",
    "/diag/ping",
    "/diag/headers",
    "/diag/alembic",
    "/diag/version",
    "/docs/openapi.html",
    "/api/users",
    "/api/courses",
    "/api/lessons",
    "/api/enrollments",
    "/api/payments",
    "/api/recommendations/cache",
    "/api/whiteboard/sessions",
]

def ping(path: str) -> str:
    try:
        with urllib.request.urlopen(BASE + path, timeout=5) as resp:
            return f"{resp.status}"
    except Exception as e:
        return f"ERR ({e.__class__.__name__})"

def main() -> int:
    for p in PATHS:
        print(f"{p:32s} -> {ping(p)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
