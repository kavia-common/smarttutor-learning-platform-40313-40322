import os
import time
import hmac
import hashlib
import base64
from typing import Optional, Dict, Any

# PUBLIC_INTERFACE
def get_jwt_secret() -> str:
    """Return JWT secret from environment.

    Do not hardcode secrets; rely on environment variables.
    """
    secret = os.getenv("JWT_SECRET", "")
    if not secret:
        raise RuntimeError("JWT_SECRET is required but not set.")
    return secret

# PUBLIC_INTERFACE
def sign_hs256(payload: Dict[str, Any], exp_seconds: int = 3600) -> str:
    """Create a minimal HS256-signed token using HMAC (lightweight placeholder).

    Note:
    - This is a minimal implementation to avoid extra deps at this stage.
    - Replace with PyJWT or authlib for production-grade JWT handling.
    """
    header = {"alg": "HS256", "typ": "JWT"}
    now = int(time.time())
    payload = {**payload, "iat": now, "exp": now + exp_seconds}

    def b64url(data: bytes) -> bytes:
        return base64.urlsafe_b64encode(data).rstrip(b"=")

    header_b64 = b64url(__to_json_bytes(header))
    payload_b64 = b64url(__to_json_bytes(payload))
    signing_input = header_b64 + b"." + payload_b64
    sig = hmac.new(get_jwt_secret().encode(), signing_input, hashlib.sha256).digest()
    token = signing_input + b"." + b64url(sig)
    return token.decode()

# PUBLIC_INTERFACE
def verify_hs256(token: str) -> Optional[Dict[str, Any]]:
    """Verify a minimal HS256 token; returns payload dict or None if invalid.

    This is a placeholder and does not handle clock skew or advanced claims.
    """
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        header_b64, payload_b64, sig_b64 = parts
        signing_input = (header_b64 + "." + payload_b64).encode()
        sig = base64.urlsafe_b64decode(__pad_b64(sig_b64))
        expected = hmac.new(get_jwt_secret().encode(), signing_input, hashlib.sha256).digest()
        if not hmac.compare_digest(sig, expected):
            return None
        import json
        payload = json.loads(base64.urlsafe_b64decode(__pad_b64(payload_b64)).decode())
        # Basic exp check
        if "exp" in payload and int(time.time()) > int(payload["exp"]):
            return None
        return payload
    except Exception:
        return None

def __to_json_bytes(obj: Dict[str, Any]) -> bytes:
    import json
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False).encode()

def __pad_b64(s: str) -> bytes:
    rem = len(s) % 4
    if rem:
        s += "=" * (4 - rem)
    return s.encode()
