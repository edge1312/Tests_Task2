import requests

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text_to_translate, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    text = text_to_translate

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    result_text = json_['text'][0]
    #result_code = response.status_code
    # print('Result_code =', result_code)

    return result_text


def define_args():
    text_to_translate = input('Введите выражение, которое необходимо перевести: ')
    to_lang = input('Укажите язык, на который необходимо перевести текст (по умолчанию "RU"): ')
    print()
    if to_lang == '':
        print(translate_it(text_to_translate))
    else:
        print(translate_it(text_to_translate, to_lang))



# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста.
# Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    define_args()
