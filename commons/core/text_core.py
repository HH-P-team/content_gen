from commons.core.api import API

class TextCore(API):
    """
    """

    def create_text(self,
                    category: str,
                    prompt: str
                    ):
        """
        """
        
        url = 'http://text_core:8000/api/v1/post/'

        return self.send_post(
            url, {
                'category': category,
                'prompt': prompt,
                })
