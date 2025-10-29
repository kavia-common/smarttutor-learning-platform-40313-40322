import hashlib
import hmac
import os
from typing import Tuple

_PEPPER = os.getenv("PWD_PEPPER", "")

# PUBLIC_INTERFACE
def hash_password(password: str, salt: str | None = None) -> Tuple[str, str]:
    """Hash a password using SHA256 with salt and optional pepper (dev utility).
    Returns (salt, hash_hex)."""
    if salt is None:
        salt = os.urandom(16).hex()
    data = (salt + password + _PEPPER).encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    return salt, digest

# PUBLIC_INTERFACE
def verify_password(password: str, salt: str, hash_hex: str) -> bool:
    """Verify password against salt and stored hash."""
    data = (salt + password + _PEPPER).encode("utf-8")
    calc = hashlib.sha256(data).hexdigest()
    return hmac.compare_digest(calc, hash_hex)
