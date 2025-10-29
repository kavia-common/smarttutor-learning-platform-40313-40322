import os
from dotenv import load_dotenv

load_dotenv()
# Use sqlite in-memory for tests
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_register_and_login_flow():
    from app import create_app
    from app.db import db
    app = create_app()
    with app.app_context():
        # Create all tables quickly for sqlite in-memory
        db.create_all()

    client = app.test_client()

    # Register
    resp = client.post("/api/auth/register", json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "secret123"
    })
    assert resp.status_code == 201, resp.data
    data = resp.get_json()
    assert "user" in data and "token" in data
    assert data["user"]["email"] == "testuser@example.com"

    # Login with correct credentials
    resp2 = client.post("/api/auth/login", json={
        "email": "testuser@example.com",
        "password": "secret123"
    })
    assert resp2.status_code == 200, resp2.data
    data2 = resp2.get_json()
    assert "user" in data2 and "token" in data2

    # Login with wrong password
    resp3 = client.post("/api/auth/login", json={
        "email": "testuser@example.com",
        "password": "wrong"
    })
    assert resp3.status_code == 401
