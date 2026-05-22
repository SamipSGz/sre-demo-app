import logging
import time
import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.routes import users, health
from app.auth.middleware import JWTMiddleware

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        start = time.time()
        response = await call_next(request)
        duration_ms = round((time.time() - start) * 1000, 2)
        logger.info(json_log(request_id, request.method,
                             str(request.url.path),
                             response.status_code, duration_ms))
        response.headers["X-Request-ID"] = request_id
        return response


def json_log(rid, method, path, status, duration_ms):
    import json
    return json.dumps({"request_id": rid, "method": method,
                       "path": path, "status": status,
                       "duration_ms": duration_ms})


app = FastAPI(title="SRE Demo App", version="1.1.0")

app.add_middleware(LoggingMiddleware)
app.add_middleware(JWTMiddleware)
app.include_router(health.router)
app.include_router(users.router, prefix="/api/v1")
