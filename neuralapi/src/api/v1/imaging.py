import os
import time
import asyncio
from http import HTTPStatus

from fastapi import Depends, HTTPException, APIRouter, Response
from aiofiles import os as aos

from schemas.inscheme import UserReq
from imageprocessor.classifier import (
    beuty_classifier,
    education_classifier,
    relax_classifier,
    restuarants_classifier,
    dress_classifier,
)

from neuro_gateway.stable_diffusion import StableDiffusion
from neuro_gateway.kandinsky import Kandinsky

from services.imageservice import (
    get_generate_sd_service,
    get_generate_kad_service,
)
from services.prefecioner import prefecioner


imaging_router = APIRouter()


@imaging_router.get(
    "/image",
    status_code=HTTPStatus.ACCEPTED,
    # dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def get_image(
    data: UserReq = Depends(),
    # common: LoginPassAnnotated = Depends(LoginPassAnnotated),
    generate_sd: list[StableDiffusion] = Depends(get_generate_sd_service),
    generate_kad: Kandinsky = Depends(get_generate_kad_service),
) -> dict:
    start = time.time()
    for filename in await aos.listdir("downloads"):
        file_path = os.path.join("downloads", filename)
        await aos.remove(file_path)

    tasks = [prefecioner(gen, data.text, "sd") for gen in generate_sd]
    tasks.append(prefecioner(generate_kad, data.text, "kd"))

    await asyncio.gather(*tasks)

    total_time = time.time() - start

    return {"resp": "OK", "time": total_time}
