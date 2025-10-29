#!/usr/bin/env python
"""
Run a quick smoke check against the Flask app using the test client.
"""
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    app = create_app()
    with app.test_client() as c:
        for path in ["/health", "/api/", "/api/ping", "/api/status"]:
            r = c.get(path)
            print(path, r.status_code, r.get_json(silent=True))
    print("Smoke check complete.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
