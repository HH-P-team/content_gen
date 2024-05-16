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

    def get_image(self, message: str):
        """
        """
        data['sdImage']['request'] = message
        resp = self.send_post(URL, data)
        id = resp[1]['message']['id']
        self.download_image_by_id(id)



    def download_image_by_id(self, id: int):
        """
        """

        params = {
            'id': id,
            'serviceType': 'sd',
        }

        res = self.send_get(DOWN_URL, params=params)

        with open('file.jpg', 'wb') as f:
            f.write(res)