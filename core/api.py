# GigaChat api
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from .config import CREDENTIALS
from post_generator.core.prompts import ROLE


class GigaChatApi:
    def __init__(self):
        self.chat = GigaChat(
            credentials=CREDENTIALS,
            verify_ssl_certs=False,
        )
        self.messages = [SystemMessage(content=ROLE)]

    def send_message(self, message: str) -> str:
        self.messages.append(HumanMessage(content=message))

        answer = self.chat(
            self.messages,
            # temperature=1,
            # top_p=1,
            # n=1,
            # max_tokens=1024,
            # repetition_penalty=1.0,
        )

        self.messages.append(answer)

        return answer.content


