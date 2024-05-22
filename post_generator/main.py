import instaloader


def main() -> None:
    
    
    pass
    # Отправить роль

    # вычленить смысл
    # лемматизация
    # удалить стоп слова
    # удалить пунктуацию
    # удалить числа
    # удалить лишние пробелы
    # удалить лишние символы
    # удалить лишние слова
    # сделать генерацию текста поста?

    input_prompt = ...
    lemma_prompt = input_prompt
    filter_prompt = lemma_prompt
    
    send_to_neuro = filter_prompt
    
    get_prompt = send_to_neuro(chat_gpt)

    check_prompt = get_prompt


if __name__ == "__main__":
    L = instaloader.Instaloader()

    for post in instaloader.Hashtag.from_name(L.context, "foodie").get_posts():
        # print(post)
        # post is an instance of instaloader.Post
        L.download_post(post, target="#foodie")

# instaloader profile catworld_id

    # main()
