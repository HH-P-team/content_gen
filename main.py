import uvicorn
import base64
from commons.config import get_settings
from sqlalchemy import select

from commons.neuro_gateway.mistral import Mistral
from commons.neuro_gateway.stable_diffusion import StableDiffusion


from commons.models import Image, Subject
from commons.db import get_db

settings = get_settings()

api_key = settings.mistral_api_key
# api = Mistral(api_key)
# res = api.send_message('5 русских волков')

# api = StableDiffusion(api_key)

# res = api.get_image_payload('Молодые колдуны')

# data = base64.b64encode(res)

# img = Image(payload=data, subject_id=1)

# for session in get_db():
#     session.add(img)
#     session.commit()

for session in get_db():
    res = session.scalar(
        select(Subject).where(Subject.name == "Бьюти индустрия1")
    )

    print(res)
    if res:
        print(res.image.payload)

# print(data)

# from collector.tasks import test_task

# test_task()

# from backend.main import app

# if __name__ == '__main__':

#     uvicorn.run(
#         'backend.main:app',
#         host="0.0.0.0",
#         port=8000, ####
#         reload=True,
#         loop='uvloop',
#     )
