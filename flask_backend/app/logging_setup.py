import logging
from flask import Flask, jsonify

# PUBLIC_INTERFACE
def setup_logging(app: Flask) -> None:
    """Configure basic logging and register a generic error handler."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")

    @app.errorhandler(Exception)
    def handle_exception(err: Exception):
        app.logger.exception("Unhandled exception: %s", err)
        return jsonify({"error": "internal_error"}), 500
