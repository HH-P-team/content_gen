from fastapi import Depends
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

from core.logger import logger
from schemas.post import Post, InputPrompt
from dependency.chat import get_chat
import core.prompts as prompts


class PostService:
    def __init__(self, chat: GigaChat):
        self.chat: GigaChat = chat

    def generate_post(self, input_prompt: InputPrompt) -> Post:
        # category dobaviyt

        system_message = (
            f"{prompts.role} {prompts.items[input_prompt.category.name]["name"]}. "
            f"{prompts.first_prompt}"
        )
        logger.info(system_message)

        messages = [
            SystemMessage(content=system_message),
        ]

        messages.append(HumanMessage(content=input_prompt.prompt))

        answer = self.chat(
            messages,
            # temperature=1,
            # top_p=1,
            # n=1,
            # max_tokens=1024,
            # repetition_penalty=1.0,
        )

        messages.append(answer)

        content = answer.content

        return Post(
            category=input_prompt.category,
            input_prompt=input_prompt.prompt,
            # result=[""],
            result=[content],
        )


def get_post_service(chat: GigaChat = Depends(get_chat)) -> PostService:
    return PostService(chat=chat)
