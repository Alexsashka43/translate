import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

def open_file(from_file):
    with open(from_file, 'r',  encoding='utf-8') as file:
        text = []
        for one_str in file:
            text.append(one_str)
        return text

def file_to_write(translated_text,to_file):
    with open(to_file, 'w', encoding='utf-8') as file:
        for string in translated_text:
            file.write(string)


def translate_it(from_file, to_file, to_lang='ru'):

    params = {
        'key': API_KEY,
        'text': open_file(from_file),
        'lang': '{}'.format(to_lang)
    }
    response = requests.get(URL, params=params)
    json_ = response.json()

    file_to_write(json_['text'],to_file)


if __name__ == '__main__':
    translate_it('ES.txt','Translate.txt','ru')
