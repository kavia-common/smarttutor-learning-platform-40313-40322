from flask import Flask
from .logging_config import configure_logging, register_request_logger

def register_logging(app: Flask) -> None:
    """Setup logging and request logger."""
    configure_logging(app)
    register_request_logger(app)
