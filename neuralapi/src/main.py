import logging
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.imaging import imaging_router
from core.settings import settings
from imageprocessor.perceptualhash import PerceptualHash
from imageprocessor.resnet import ResNet


from imageprocessor.classifier import (
    beuty_classifier,
    education_classifier,
    relax_classifier,
    restuarants_classifier,
    dress_classifier,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    beuty_phash = PerceptualHash("datasets/beuty/2021")
    beuty_resnet = ResNet("datasets/beuty/2021")
    beuty_classifier.add_processor(beuty_phash)
    beuty_classifier.add_processor(beuty_resnet)


app = FastAPI(
    title=settings.app_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


app.include_router(
    imaging_router,
    prefix=f"/api/v1/{settings.app_name}",
    tags=[f"{settings.app_name}"],
)


if __name__ == "__main__":
    logging.info("start neuralapi-service")
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        log_level="debug",
        reload=True,
    )
