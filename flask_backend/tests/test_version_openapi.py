import os
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_version_and_openapi_match():
    from app import create_app
    from app.constants import APP_VERSION, APP_NAME
    from app.db import db
    app = create_app()
    with app.app_context():
        db.create_all()
    client = app.test_client()

    res = client.get("/api/version")
    assert res.status_code == 200
    data = res.get_json()
    assert data["version"] == APP_VERSION
    assert data["name"] == APP_NAME

    res2 = client.get("/openapi.json")
    assert res2.status_code == 200
    spec = res2.get_json()
    assert spec["info"]["version"] == APP_VERSION
