from __future__ import annotations
from typing import Tuple
from flask import request

DEFAULT_LIMIT = 50
MAX_LIMIT = 200

# PUBLIC_INTERFACE
def get_pagination_params() -> Tuple[int, int]:
    """Extract pagination parameters (limit, offset) from query string.

    Query params:
      - limit: int (default 50, max 200)
      - offset: int (default 0)

    Returns:
      (limit, offset) tuple validated and clamped to sane bounds.
    """
    limit = request.args.get("limit", type=int) or DEFAULT_LIMIT
    offset = request.args.get("offset", type=int) or 0
    if limit < 1:
        limit = DEFAULT_LIMIT
    if limit > MAX_LIMIT:
        limit = MAX_LIMIT
    if offset < 0:
        offset = 0
    return limit, offset
