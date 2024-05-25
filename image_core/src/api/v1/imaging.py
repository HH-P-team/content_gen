import os
import time
import asyncio
from http import HTTPStatus

from fastapi import Depends, APIRouter
from fastapi.responses import FileResponse
from aiofiles import os as aos

from core.settings import settings
from schemas.inscheme import UserReq
from schemas.outscheme import ImageResp

from neuro_gateway.stable_diffusion import StableDiffusion

from neuro_gateway.fusionbrain import Fusionbrain

from services.imageservice import (
    get_generate_sd_service,
    get_generate_fb_service,
)
from services.prefecioner import prefecioner
from imageprocessor.classifier import classifier_matrix
from services.imagingservice import acopy

imaging_router = APIRouter()


@imaging_router.get(
    "/image",
    status_code=HTTPStatus.ACCEPTED,
    response_model=ImageResp,
)
async def get_image(
    input: UserReq = Depends(),
    generate_sd: list[StableDiffusion] = Depends(get_generate_sd_service),
    generate_fb: Fusionbrain = Depends(get_generate_fb_service),
) -> dict:
    start = time.time()
    for filename in await aos.listdir(settings.path_to_downloads):
        file_path = os.path.join(settings.path_to_downloads, filename)
        await aos.remove(file_path)

    negative = "текст, слова, фразы, надписи"
    tasks = []
    # tasks = [
    #     prefecioner(gen, input.text, negative, "sd") for gen in generate_sd
    # ]

    classificator = classifier_matrix.get(input.category)

    if classificator:
        tasks.extend(
            [
                prefecioner(generate_fb, input.text, negative, "fb")
                for i in range(5)
            ]
        )
        await asyncio.gather(*tasks)

        classification = classificator.get_classification(
            settings.path_to_downloads
        )
        files = list(classification.keys())
    else:
        tasks = [prefecioner(generate_fb, input.text, negative, "fb")]
        await asyncio.gather(*tasks)
        classification = {}
        files = await aos.listdir(settings.path_to_downloads)

    total_time = time.time() - start

    down_file = f"{settings.path_to_downloads}/{files[0]}"
    art_file = f"{settings.path_to_arts}/{input.uuid}.jpg"

    if not input.file:

        await acopy(down_file, art_file)

        return {
            "promt": input.text,
            "time": total_time,
            "classification": classification,
            "path": art_file,
            "uuid": input.uuid,
        }

    else:

        return FileResponse(
            path=down_file,
            filename=files[0],
            media_type="multipart/form-data",
        )
