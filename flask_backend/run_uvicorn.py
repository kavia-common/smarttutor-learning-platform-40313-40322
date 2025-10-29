#!/usr/bin/env python
"""
Run the Flask WSGI app using Uvicorn's WSGIMiddleware for local testing.
Not intended for production (use Gunicorn).
"""
import os
from uvicorn import run
from starlette.middleware.wsgi import WSGIMiddleware
from wsgi import app as flask_app

def main():
    os.environ.setdefault("PORT", "8000")
    application = WSGIMiddleware(flask_app)
    run(application, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

if __name__ == "__main__":
    main()
