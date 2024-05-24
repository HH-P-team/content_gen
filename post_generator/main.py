from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models.gigachat import GigaChat

from routes import routes
from dependency import chat
from core.config import CREDENTIALS
from core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting")
    chat.chat = GigaChat(
        credentials=CREDENTIALS,
        verify_ssl_certs=False,
    )

    yield
    logger.info("Closing")


app = FastAPI(
    lifespan=lifespan,
    openapi_url="/api/openapi.json",
    docs_url="/api/openapi",
    redoc_url=None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes)
