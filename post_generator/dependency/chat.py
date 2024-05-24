from langchain.chat_models.gigachat import GigaChat


chat: GigaChat | None = None


def get_chat() -> GigaChat:
    yield chat
