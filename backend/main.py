from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.routers import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.include_router(router)
    yield

app = FastAPI(
    lifespan=lifespan,
)


if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000, ####
        reload=True,
        loop='uvloop',
    )