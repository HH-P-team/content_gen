from typing import Optional, Tuple

from pymystem3 import Mystem

from dialog.abstract_dialog import BaseDialog
from dialog.exceptions import DialogKeywordNotFound
from dialog.keywords import all_keywords


class Dialog(BaseDialog):
    def parse_text(self, text: str) -> Tuple[str, str, Optional[str]]:
        """
        Обработка текста для определения по какому полю искать в Elasticsearch.
        params:
            text: str - строка с текстом диалога
        return:
            what_return: str - какой поле возвращать пользователю
            where_search: str - по какому полю производить поиск
            what_search: str - значение для поиска
        """

        m = Mystem()
        lemmas = m.lemmatize(text)
        lemmas = [lemma for lemma in lemmas if not lemma.isspace()]

        keywords = [lemma for lemma in lemmas if lemma in all_keywords.keys()]

        if not keywords:
            raise DialogKeywordNotFound(f"Can not found keyword in the text: {text}")

        last_index = lemmas.index(keywords[-1])
        first_index = lemmas.index(keywords[0])

        text_list = text.split()

        if last_index == len(text_list) - 1 and len(keywords) == 1:
            return (
                all_keywords[lemmas[last_index]],
                all_keywords[lemmas[last_index]],
                None,
            )

        value: Optional[str] = " ".join(text.split()[last_index + 1 :])
        if not value:
            value = None

        if lemmas[last_index] == "title" and len(keywords) != 1:
            return (
                all_keywords[lemmas[last_index]],
                all_keywords[lemmas[first_index]],
                value,
            )

        return (
            all_keywords[lemmas[first_index]],
            all_keywords[lemmas[last_index]],
            value,
        )