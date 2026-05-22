import jwt
from datetime import datetime, timedelta
from app.auth.middleware import SECRET_KEY, ALGORITHM


def create_access_token(user_id: int, expires_minutes: int = 60) -> str:
    payload = {
        "sub": str(user_id),
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
