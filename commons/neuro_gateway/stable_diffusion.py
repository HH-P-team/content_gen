import base64

from commons.neuro_gateway.api import API

URL = 'https://ai.rt.ru/api/1.0/sd/img'
DOWN_URL = 'https://ai.rt.ru/api/1.0/download'

data = {
  'sdImage': {
    'translate': True,
    'request': None
  }
}

class StableDiffusion(API):
    """
    """

    def get_image_payload(self, message: str) -> bytes:
        id = self.get_image_id(message)
        return self.get_image_payload_by_id(id)
    
    def get_image_payload_b64(self, message: str) -> bytes:
        id = self.get_image_id(message)
        res = self.get_image_payload_by_id(id)
        return base64.b64encode(res)

    def get_image_id(self, message: str) -> int:
        """
        """
        data['sdImage']['request'] = message
        resp = self.send_post(URL, data)
        return resp[1]['message']['id']

    def get_image(self,
                  message: str,
                  filepath: str,
                  filename: str) -> None:
        """
        """
        id = self.get_image_id(message)
        self.download_image_by_id(id, filepath, filename)

    def get_image_payload_by_id(self, id: int) -> bytes:
        params = {
            'id': id,
            'serviceType': 'sd',
        }

        return self.send_get(DOWN_URL, params=params)

    def download_image_by_id(self,
                             id: int,
                             filepath: str,
                             filename: str) -> None:
        """
        """

        res = self.get_image_payload_by_id(id)

        with open(f'{filepath}/{filename}.png', 'wb') as f:
            f.write(res)