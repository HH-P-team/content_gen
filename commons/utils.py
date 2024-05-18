from commons.neuro_gateway.mistral import Mistral


def get_products(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Придумай названия 5 коммерческих продуктов подходящих под категорию {subject}'
        )

def get_post_description(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Напиши пост рекламного характера на следующую тематику: {subject}'
        )
