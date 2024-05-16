import requests

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': None,
    'Content-Type': 'application/json',
}

class API:
    """
    """
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def send_post(self, URL, data) -> dict:
        """
        """
        headers['Authorization'] = f'Bearer {self.api_key}'
        resp = requests.post(url=URL, headers=headers, json=data)

        if resp.status_code == 200:
             return resp.json()
        else:
            raise Exception(resp.text)
        
    def send_get(self, URL, params) -> bytes:
        """
        """
        headers['Authorization'] = f'Bearer {self.api_key}'
        resp = requests.get(url=URL, headers=headers, params=params)

        if resp.status_code == 200:
             return resp.content
        else:
            raise Exception(resp.text)