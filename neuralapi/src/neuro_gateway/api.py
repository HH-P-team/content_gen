from http import HTTPStatus

import httpx

from core.settings import settings, logger

headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": None,
    "Content-Type": "application/json",
}


class API:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    async def send_post(self, URL, data) -> dict:
        headers["Authorization"] = f"Bearer {self.api_key}"
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    url=URL,
                    headers=headers,
                    json=data,
                    timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            logger.error(e)

        if resp.status_code == HTTPStatus.OK:
            return resp.json()
        else:
            raise Exception(resp.text)

    async def send_get(self, URL, params=None) -> bytes:
        headers["Authorization"] = f"Bearer {self.api_key}"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    url=URL,
                    headers=headers,
                    params=params,
                    timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            logger.error(e)

        if resp.status_code == HTTPStatus.OK:
            return resp.content
        else:
            raise Exception(resp.text)
