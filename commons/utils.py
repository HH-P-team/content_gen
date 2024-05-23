from commons.neuro_gateway.mistral import Mistral

def get_product(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Действуй в качестве маркетолога, выполни задачу придумай название коммерческого продукта, подходящего под категорию {subject}. В виде названия не более 3 слов'
        )

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

