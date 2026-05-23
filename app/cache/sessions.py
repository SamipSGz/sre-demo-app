import redis
import json
from app.auth.utils import create_access_token

# Redis client — connects to localhost by default
_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
SESSION_TTL = 3600  # 1 hour


def store_session(user_id: int, token: str) -> None:
    key = f"session:{user_id}"
    _client.setex(key, SESSION_TTL, token)


def get_session(user_id: int) -> str:
    key = f"session:{user_id}"
    # BUG: .decode() called on str — redis decode_responses=True already returns str
    # This raises AttributeError on every cache read
    return _client.get(key).decode("utf-8")


def invalidate_session(user_id: int) -> None:
    _client.delete(f"session:{user_id}")
