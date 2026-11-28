import logging
from time import time
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.concurrency import run_in_threadpool

from app.api.routes import audit, health, security
from app.core.config import get_settings
from app.core.rate_limit import increment_request_count
from app.db.session import engine

logger = logging.getLogger(__name__)
settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url=None,
    openapi_url="/openapi.json" if settings.app_env != "production" else None,
)


@app.middleware("http")
async def request_context_and_security_headers(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", "")
    if not request_id or len(request_id) > 80 or not request_id.replace("-", "").replace("_", "").isalnum():
        request_id = str(uuid4())
    request.state.request_id = request_id

    response = None
    if request.url.path.startswith("/api/v1/"):
        client_host = request.client.host if request.client else None
        try:
            count, reset_at = await run_in_threadpool(
                increment_request_count,
                engine,
                client_host=client_host,
                now=int(time()),
                window_seconds=settings.api_rate_limit_window_seconds,
            )
        except SQLAlchemyError:
            # Fail closed: do not silently disable the API rate limit when its store is unavailable.
            logger.error("API rate-limit storage unavailable; request denied")
            response = JSONResponse(
                status_code=503,
                content={"detail": "API protection is temporarily unavailable", "request_id": request_id},
            )
        else:
            limit = settings.api_rate_limit_requests_per_minute
            remaining = max(0, limit - count)
            if count > limit:
                retry_after = max(1, reset_at - int(time()))
                response = JSONResponse(
                    status_code=429,
                    content={"detail": "Rate limit exceeded", "request_id": request_id},
                    headers={"Retry-After": str(retry_after)},
                )
            else:
                response = await call_next(request)
            response.headers["RateLimit-Limit"] = str(limit)
            response.headers["RateLimit-Remaining"] = str(remaining)
            response.headers["RateLimit-Reset"] = str(max(0, reset_at - int(time())))
    else:
        response = await call_next(request)

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Cache-Control"] = "no-store"
    if not request.url.path.startswith(("/docs", "/openapi.json")):
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
    if settings.app_env == "production":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response


@app.exception_handler(RequestValidationError)
async def safe_validation_error(request: Request, exc: RequestValidationError):
    # Do not echo rejected input values: request bodies may later contain sensitive data.
    errors = [
        {"location": [str(part) for part in item.get("loc", [])], "type": item.get("type", "invalid")}
        for item in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={"detail": "Request validation failed", "errors": errors, "request_id": request.state.request_id},
        headers={"Cache-Control": "no-store", "X-Request-ID": request.state.request_id},
    )


app.include_router(health.router)
app.include_router(security.router)
app.include_router(audit.router)
