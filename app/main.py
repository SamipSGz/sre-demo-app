from fastapi import FastAPI
from app.routes import users, health
from app.auth.middleware import JWTMiddleware

app = FastAPI(title="SRE Demo App", version="1.0.0")

app.add_middleware(JWTMiddleware)
app.include_router(health.router)
app.include_router(users.router, prefix="/api/v1")
