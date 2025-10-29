import os
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_version_endpoint():
    from app import create_app
    from app.db import db
    from app.constants import APP_NAME

    app = create_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    res = client.get("/api/version")
    assert res.status_code == 200
    data = res.get_json()
    assert "name" in data and "version" in data
    assert data["name"] == APP_NAME
