import logging
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.imaging import imaging_router
from core.settings import settings
from imageprocessor.perceptualhash import PerceptualHash
from imageprocessor.resnet import ResNet


from imageprocessor.classifier import classifier_matrix


@asynccontextmanager
async def lifespan(app: FastAPI):
    for category, classifier in classifier_matrix.items():
        classifier.add_processor(
            PerceptualHash(
                settings.__getattribute__(f"dataset_{category}_path")
            )
        )
        classifier.add_processor(
            ResNet(settings.__getattribute__(f"dataset_{category}_path"))
        )

    yield


app = FastAPI(
    title=settings.app_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
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
