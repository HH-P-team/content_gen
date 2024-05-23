from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.base import router

origins = [
    "*",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.include_router(router)
    yield


app = FastAPI(
    lifespan=lifespan,
    openapi_url="/api/openapi"
)

app.mount(
    "/product_images",
    StaticFiles(directory="staticfiles"),
    name="staticfiles",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
