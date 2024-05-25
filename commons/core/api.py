from http import HTTPStatus
import requests

import httpx


class API:
    """
    """

    async def async_send_post(self, URL, data) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    url=URL,
                    json=data,
                    # timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            pass

        if resp.status_code == HTTPStatus.OK:
            return resp.json()
        else:
            raise Exception(resp.text)

    async def async_send_get(self, URL, params=None) -> bytes:
        # headers["Authorization"] = f"Bearer {self.api_key}"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    url=URL,
                    # headers=headers,
                    params=params,
                    # timeout=settings.ext_api_timeout,
                )
        except httpx.ReadTimeout as e:
            # logger.error(e)
            pass

        if resp.status_code == HTTPStatus.OK:
            return resp.content
        else:
            raise Exception(resp.text)
        

    def send_get(self, URL, data) -> dict:
        
        resp = requests.get(url=URL, params=data)

        # if resp.status_code == HTTPStatus.OK:
        return resp.content
        # else:
        #     print(resp.status_code)
            # raise Exception(resp.text)

    def send_post(self, URL, data) -> dict:
        
        resp = requests.post(url=URL, json=data)

        # if resp.status_code == HTTPStatus.OK:
        return resp.json()
        # else:
        #     print(resp.status_code)
            # raise Exception(resp.text)
