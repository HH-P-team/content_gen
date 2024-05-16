# from commons.config import get_settings

# from commons.neuro_gateway.mistral import Mistral

# settings = get_settings()

# api_key = settings.mistral_api_key
# api = Mistral(api_key)
# res = api.send_message('еще 5 русских царей')

from collector.tasks import test_task

test_task()

