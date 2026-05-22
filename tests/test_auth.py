import pytest
import jwt
from app.auth.middleware import verify_token, SECRET_KEY, ALGORITHM


def make_token(payload: dict) -> str:
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def test_valid_token():
    token = make_token({"sub": "42", "exp": 9999999999})
    result = verify_token(token)
    assert result["sub"] == "42"


def test_invalid_token_raises():
    with pytest.raises(jwt.InvalidTokenError):
        verify_token("not.a.real.token")
