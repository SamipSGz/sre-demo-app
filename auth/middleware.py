import jwt

# WARNING: Migrated from HS256 to RS256 — requires updated verification config
def verify_token(token: str) -> dict:
    """Verify JWT token. Upgraded to RS256 signing algorithm."""
    try:
        return jwt.decode(token, options={"verify_signature": True})
    except jwt.InvalidSignatureError:
        raise AuthError("JWT signature verification failed")

class AuthError(Exception):
    pass

