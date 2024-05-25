from gigachat import GigaChat

from core.settings import settings


class VladlenTatarsky:
    def __init__(self, token):
        self.token = token

    def get_background(self, assist, text, action=0):

        response = assist.chat(
            (
                f"текст: {text}. предложи описание лучшего "
                "варианта фона для изображения не должно быть логотипов"
            )
        )

        response = assist.chat(
            (
                f"текст: {response.choices[0].message.content}. "
                "основные объекты пронумеруй"
            )
        )

        background = response.choices[0].message.content.split("\n")

        background_promts = []
        for promt in background:

            if "извините" in promt.lower() or promt == "":
                continue

            background_promts.append(promt)

        if not background_promts and action == 0:
            background_promts.extend(
                self.get_background(assist, text, action=1)
            )

        if not background_promts:
            background_promts.append("придумай красиый фон")

        if len(background_promts) == 1:
            background_promts = ["придумай красиый фон"]
        return background_promts

    def get_subject(self, assist, text, action=0):

        response = assist.chat(
            (
                f"текст: {text}. предложи варианты описания "
                "объектов для изображения не должно быть логотипов"
            )
        )

        response = assist.chat(
            (
                f"текст: {response.choices[0].message.content}."
                " основные объекты пронумеруй"
            )
        )

        obj = response.choices[0].message.content.split("\n")

        obj_promts = []

        for promt in obj:
            if (
                "извините" in promt.lower()
                or promt == ""
                or "объекты" in promt.lower()
            ):
                continue
            sub_promt = promt.split(";")
            for s_promt in sub_promt:
                obj_promts.append(s_promt)

        if not obj_promts and action == 0:
            obj_promts.extend(self.get_subject(assist, text, action=1))

        return obj_promts

    def get_style(self, assist, text, styles, action=0):

        str_styles = ", ".join(styles)
        response = assist.chat(
            (
                f"текст: {text}. предложи описание лучшего варианта стиль для"
                " изображения который лучше применть из вариантов:"
            )
            + str_styles
        )

        st = response.choices[0].message.content.split("\n")

        result = []
        for item in st:
            for my_st in styles:
                if my_st in item:
                    result.append(my_st)

        if not result:
            result = ["классика"]

        return result

    def promt_creator(self, background, obj, style):

        check = background.split()

        if check[0].isdigit:
            ln = len(check[0])
            background = background[ln:]

        check = obj.split()

        if check[0].isdigit:
            ln = len(check[0]) + 1
            obj = obj[ln:]

        return f"фон: {background}, объект: {obj}, стиль: {style}"

    def generate_promts(self, text):
        with GigaChat(credentials=self.token, verify_ssl_certs=False) as giga:
            styles = [
                "анимэ",
                "классика",
                "искусство",
                "модерн",
                "мультипликация",
                "молодёжный",
            ]

            backgrounds = self.get_background(giga, text)
            objs = self.get_subject(giga, text)
            sts = self.get_style(giga, text, styles)

        promts = []

        for background in backgrounds:
            if background == "":
                continue
            for obj in objs:
                if obj == "":
                    continue
                for st in sts:
                    if st == "":
                        continue
                    if len(promts) == 5:
                        break
                    promts.append(self.promt_creator(background, obj, st))
                if len(promts) == 5:
                    break
            if len(promts) == 5:
                break

        while len(promts) < 5:
            promts.append(self.promt_creator(backgrounds[0], objs[0], sts[0]))

        return promts


def get_promt_service():
    return VladlenTatarsky(settings.giga_key)
