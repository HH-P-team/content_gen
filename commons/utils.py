from commons.neuro_gateway.mistral import Mistral


def get_post_description(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Напиши пост рекламного характера на следующую тематику: {subject}'
        )