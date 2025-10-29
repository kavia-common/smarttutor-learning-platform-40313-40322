Adding routes and CORS

- API routes are defined in app/api.py within the "api" blueprint mounted at /api.
- CORS is configured in app/bootstrap.py for /api/*.
- The helper app/_init_hook.py provides a run(app) function that attaches routes and extensions.

To ensure routes are active, import and call the hook in app/__init__.py:

    from ._init_hook import run as _attach
    _attach(app)

This call should be placed after app = Flask(__name__) and configuration loading.
