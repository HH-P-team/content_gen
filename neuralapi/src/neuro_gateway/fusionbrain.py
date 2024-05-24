import os
import base64
import json
import asyncio
from http import HTTPStatus

import httpx
import aiofiles

from core.settings import settings, logger


class Fusionbrain:

    url = "https://api-key.fusionbrain.ai/"

    def __init__(self, api_key: str, secret_key: str, downloads_path: str):

        self.dpwnload_path = downloads_path
        self.auth_headers = {
            "X-Key": f"Key {api_key}",
            "X-Secret": f"Secret {secret_key}",
        }

        self.model = self._get_model()

    def _get_model(self):
        model = asyncio.run(self.get_model())

        return model

    async def get_model(self):

        model_url = self.url + "key/api/v1/models"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    url=model_url,
                    headers=self.auth_headers,
                    timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            logger.error(e)
        if resp.status_code == HTTPStatus.OK:
            data = resp.json()
            return data[0]["id"]
        else:
            raise Exception(resp.text)

    async def generate(
        self,
        prompt: str,
        model: int,
        negative: str,
        images: int = 1,
        width: int = 1024,
        height: int = 1024,
    ):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "style": "UHD",
            "negativePromptUnclip": negative,
            "generateParams": {"query": f"{prompt}"},
        }

        data = {
            "model_id": (None, json.dumps(model)),
            "params": (None, json.dumps(params), "application/json"),
        }

        gen_url = self.url + "key/api/v1/text2image/run"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    url=gen_url,
                    headers=self.auth_headers,
                    files=data,
                    params=params,
                    timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            logger.error(e)

        if resp.status_code == HTTPStatus.CREATED:
            result = resp.json()
            return result["uuid"]
        else:
            raise Exception(resp.text)

    async def check_generation(
        self, request_id: str, attempts: int = 100, delay: int = 3
    ):
        check_url = self.url + "key/api/v1/text2image/status/" + request_id

        while attempts > 0:

            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.get(
                        url=check_url,
                        headers=self.auth_headers,
                        timeout=settings.ext_api_timeout,
                    )
            except httpx.ReadTimeout as e:
                logger.error(e)

            result = resp.json()
            if result.get("status") == "DONE":
                return result["images"]

            attempts -= 1
            await asyncio.sleep(delay)

    async def get_image(
        self, text: str, negative: str, file_name: str
    ) -> None:

        file_path = os.path.join(self.dpwnload_path, file_name)

        genid = await self.generate(
            prompt=text,
            negative=negative,
            model=self.model,
        )

        image = await self.check_generation(genid)

        if image:
            async with aiofiles.open(file_path, "wb") as f:
                await f.write(base64.b64decode(image[0]))
        else:
            logger.info("external service did not send the file")
