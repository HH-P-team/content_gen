import base64

import aiofiles

from neuro_gateway.api import API

URL = "https://ai.rt.ru/api/1.0/kandinsky/img"

data = {
    "uuid": "00000000-0000-0000-0000-000000000000",
    "kandinskyImage": {
        "query": None,
        "style": "string",
        "negativePrompt": "string",
        "width": 1024,
        "height": 1024,
        "translate": True,
    },
}


class Kandinsky(API):
    """ """

    def __init__(self, key: str, download_path: str):
        super().__init__(key)
        self.download_path = download_path

    def get_url(self, id):
        return (
            f"https://ai.rt.ru/api/1.0/download?id={id}&serviceType=kandinsky"
        )

    async def get_image_payload(self, message: str) -> bytes:
        id = await self.get_image_id(message)
        return self.get_image_payload_by_id(id)

    async def get_image_payload_b64(self, message: str) -> bytes:
        id = await self.get_image_id(message)
        res = await self.get_image_payload_by_id(id)
        return base64.b64encode(res)

    async def get_image_id(self, message: str) -> int:
        """ """
        data["kandinskyImage"]["query"] = message
        resp = await self.send_post(URL, data)
        return resp[1]["message"]["id"]

    async def get_image(self, message: str, file_name: str) -> None:
        """ """
        id = await self.get_image_id(message)
        await self.download_image_by_id(id, file_name)

    async def get_image_payload_by_id(self, id: int) -> bytes:

        download_url = self.get_url(id)
        return await self.send_get(download_url)

    async def download_image_by_id(self, id: int, file_name: str) -> None:
        """ """

        res = await self.get_image_payload_by_id(id)

        async with aiofiles.open(
            self.download_path + f"/{file_name}", "wb"
        ) as f:
            await f.write(res)
