# sre-demo-app

Production FastAPI service powering authentication and user management for the platform.

## Stack
- Python 3.11 + FastAPI 0.111
- PyJWT for token signing/verification
- PostgreSQL via SQLAlchemy
- Redis for session caching
- GitHub Actions CI

## Running locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Architecture
```
app/
├── main.py          # FastAPI entrypoint + middleware wiring
├── auth/
│   ├── middleware.py  # JWT verification (JWTMiddleware)
│   └── utils.py       # Token generation helpers
├── routes/
│   ├── users.py       # /api/v1/users/* endpoints
│   └── health.py      # /health endpoint
└── models/
    └── user.py        # Pydantic user models
```
