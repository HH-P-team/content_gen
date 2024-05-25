from commons.core.api import API

class ImageCore(API):

    def create_image(self,
                     uuid: str,
                     text: str,
                     category: str='free'):
        """
        """
        
        url = 'http://image_core:8012/api/v1/image_core/image'

        return self.send_get(
                url, {
                    'uuid': uuid,
                    'text': text,
                    'category': category,
                })
