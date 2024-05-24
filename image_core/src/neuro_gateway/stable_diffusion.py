import base64

import aiofiles

from neuro_gateway.api import API

URL = "https://ai.rt.ru/api/1.0/sd/img"
DOWN_URL = "https://ai.rt.ru/api/1.0/download"

data = {"sdImage": {"translate": True, "request": None}}


class StableDiffusion(API):
    """ """

    def __init__(self, key: str, download_path: str):
        super().__init__(key)
        self.download_path = download_path

    async def get_image_payload(self, message: str) -> bytes:
        id = await self.get_image_id(message)
        return self.get_image_payload_by_id(id)

    async def get_image_payload_b64(self, message: str) -> bytes:
        id = await self.get_image_id(message)
        res = await self.get_image_payload_by_id(id)
        return base64.b64encode(res)

    async def get_image_id(self, message: str) -> int:
        """ """
        data["sdImage"]["request"] = message
        resp = await self.send_post(URL, data)
        return resp[1]["message"]["id"]

    async def get_image(
        self, message: str, negative: str, file_name: str
    ) -> None:
        """ """
        id = await self.get_image_id(message)
        await self.download_image_by_id(id, file_name)

    async def get_image_payload_by_id(self, id: int) -> bytes:
        params = {
            "id": id,
            "serviceType": "sd",
        }

        return await self.send_get(DOWN_URL, params=params)

    async def download_image_by_id(self, id: int, file_name: str) -> None:
        """ """

        res = await self.get_image_payload_by_id(id)

        async with aiofiles.open(
            self.download_path + f"/{file_name}", "wb"
        ) as f:
            await f.write(res)
