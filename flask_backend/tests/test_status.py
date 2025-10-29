import os
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_status_endpoint_keys():
    from app import create_app
    from app.db import db
    app = create_app()
    with app.app_context():
        db.create_all()
    client = app.test_client()
    res = client.get("/api/status")
    assert res.status_code == 200
    data = res.get_json()
    for key in [
        "users","courses","lessons","enrollments",
        "chat_messages","whiteboard_sessions","whiteboard_events",
        "payments","recommendations_cache"
    ]:
        assert key in data
        assert isinstance(data[key], int)
