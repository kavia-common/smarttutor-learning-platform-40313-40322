ASGI Notes

- The backend is a Flask WSGI app. For certain proxy setups or local testing, you can run it behind Uvicorn using Starlette's WSGIMiddleware.
- This is not for production; use Gunicorn for deployment.

Run locally:
  python run_uvicorn.py
  # http://localhost:8000/health

Dependencies:
- uvicorn and starlette are included in requirements.txt to support this helper.
