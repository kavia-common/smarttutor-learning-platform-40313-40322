#!/usr/bin/env python
"""
End-to-end smoke using HTTP client against a running backend on localhost:8000.

Requires: pip install requests
"""
import os
import json
import requests

API = os.environ.get("API_BASE", "http://localhost:8000/api")

def main() -> int:
    # Register (idempotent behavior handled by login fallback)
    r = requests.post(f"{API}/auth/register", json={
        "name": "E2E Tester",
        "email": "e2e@example.com",
        "password": "secret123"
    })
    if r.status_code not in (200, 201, 409):
        print("Register failed:", r.status_code, r.text)
        return 1

    # Login
    r = requests.post(f"{API}/auth/login", json={
        "email": "e2e@example.com",
        "password": "secret123"
    })
    if r.status_code != 200:
        print("Login failed:", r.status_code, r.text)
        return 1
    token = r.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}

    # Profile
    rp = requests.get(f"{API}/profile/", headers=headers)
    print("Profile:", rp.status_code, rp.json())

    # Courses
    rc = requests.get(f"{API}/courses/")
    print("Courses:", rc.status_code, len(rc.json()) if rc.ok else rc.text)

    # Create payment stub for first user and first course if present
    users = requests.get(f"{API}/users/").json()
    courses = rc.json()
    if users and courses:
        payload = {
            "user_id": users[0]["id"],
            "course_id": courses[0]["id"],
            "amount": 9.99,
            "currency": "USD",
            "provider": "stub",
            "reference": "e2e"
        }
        pay = requests.post(f"{API}/payments/", headers=headers, json=payload)
        print("Create payment:", pay.status_code, pay.json() if pay.ok else pay.text)
    else:
        print("Skipping payment creation (no users or courses).")

    print("E2E HTTP smoke finished.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
