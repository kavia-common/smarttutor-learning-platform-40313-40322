#!/usr/bin/env python
"""
Print commonly used backend URLs based on current PORT and host.
"""
import os

def main() -> int:
    port = os.getenv("PORT", "8000")
    host = os.getenv("HOST", "http://localhost")
    base = f"{host}:{port}"
    print("Base:", base)
    print("Health:", f"{base}/health")
    print("Status:", f"{base}/api/status")
    print("Version:", f"{base}/api/version")
    print("OpenAPI:", f"{base}/openapi.json")
    print("Routes:", f"{base}/api/diag/routes")
    print("WS Help:", f"{base}/api/ws-help")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
