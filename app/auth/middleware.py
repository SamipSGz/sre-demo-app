import jwt
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

ALGORITHM = "HS256"
SECRET_KEY = "super-secret-key"

EXCLUDED_PATHS = ["/health", "/docs", "/openapi.json"]


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)
        token = request.headers.get("Authorization", "").removeprefix("Bearer ")
        if not token:
            raise HTTPException(status_code=401, detail="Missing token")
        try:
            payload = verify_token(token)
            request.state.user = payload
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
        return await call_next(request)


def verify_token(token: str) -> dict:
    """Verify JWT using HS256. Returns decoded payload."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
