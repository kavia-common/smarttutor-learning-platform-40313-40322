"""
Run the Flask backend in dev mode.

Usage:
  python run_dev.py
"""
from __future__ import annotations

import os
from app import create_app
from app import __dict__ as app_pkg_dict

app = create_app()
_socketio = app_pkg_dict.get("socketio")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    if _socketio is not None:
        _socketio.run(app, host="0.0.0.0", port=port, debug=True)
    else:
        app.run(host="0.0.0.0", port=port, debug=True)
