from uuid import uuid4

from aiofiles import os as aos

from neuro_gateway.api import API
from ianalyzer.analizer import Ianalizer

analizer = Ianalizer()


async def prefecioner(generate: API, text: str, negative: str, tag: str):

    file_name = f"{tag}_{uuid4()}.jpg"
    await generate.get_image(text, negative, file_name)

    analizer_res = analizer.image_classifier(f"downloads/{file_name}")
    if tag == "sd":
        if (score := analizer_res[0]["score"]) < 0.9:
            await aos.remove(f"downloads/{file_name}")
        else:
            await aos.rename(
                f"downloads/{file_name}",
                f"downloads/{file_name[:6]}_{score}.jpg",
            )
    else:
        if (score := analizer_res[0]["score"]) < 0.5:
            await aos.remove(f"downloads/{file_name}")
        else:
            await aos.rename(
                f"downloads/{file_name}",
                f"downloads/{file_name[:6]}_{score}.jpg",
            )

    # if len(await aos.listdir("downloads")) < 5:
    #     await prefecioner(generate, text, negative, tag)
