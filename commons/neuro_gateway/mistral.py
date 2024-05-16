import requests

from pydantic import BaseModel

from commons.neuro_gateway.api import API

URL = 'https://ai.rt.ru/api/1.0/mistral/chat_universal'

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': None,
    'Content-Type': 'application/json',
}

data = {
    'chat': {
        'user_messange': None,
        'messages': [],
        'chat_history': []
    }
}

class Mistral(API):
    """
    """
    def send_message(self, message: str) -> str:
        """
        """
        headers['Authorization'] = f'Bearer {self.api_key}'
        data['chat']['user_messange'] = message
        resp = requests.post(url=URL, headers=headers, json=data)

        if resp.status_code == 200:
             return resp.json()[0]['message']['content']
        else:
            raise Exception(resp.text)