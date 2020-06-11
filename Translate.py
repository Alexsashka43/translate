import requests


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


def read_data(file_name):
    text = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for i in f:
            text.append(i)
    return text
text = read_data('FR.txt')
# print(text)



def translate_it(text, to_lang):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])
    json = translate_it(text, fr)


translated = translate_it(text, 'fr')
# print(translated)

with open('Translated.txt', 'w', encoding='utf-8') as translate:
    translate.write(translated)

if __name__ == '__main__':
    pass

    # print(translate_it(text, 'fr'))
