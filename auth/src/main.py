import logging
import uvicorn

import redis.asyncio as redis

from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse
from fastapi_limiter import FastAPILimiter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from alembic.config import Config
from alembic import command


from helpers.tracer import configure_tracer
from core.settings import settings
from api.v1 import authorization


configure_tracer()
app = FastAPI(
    title=settings.project_name,
    docs_url="/auth/api/openapi",
    openapi_url="/auth/api/openapi.json",
    default_response_class=ORJSONResponse,
)
# FastAPIInstrumentor.instrument_app(app)


@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

    cache_limiter = redis.from_url(
        f"redis://{settings.redis_host}:{settings.redis_port}",
        password=settings.redis_password,
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(cache_limiter)


@app.middleware("http")
async def before_request(request: Request, call_next):
    response = await call_next(request)
    request_id = request.headers.get("X-Request-Id")
    if not request_id:
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "X-Request-Id is required"},
        )
    return response


app.include_router(
    authorization.router,
    prefix="/auth/api/v1/authorization",
    tags=["authorization"],
)


if __name__ == "__main__":
    logging.info("start auth service")
    uvicorn.run(
        "main:app",
        host=settings.auth_host,
        port=settings.auth_port,
        reload=True,
    )
