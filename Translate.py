import requests


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

def translate_it(from_file, to_file, from_lng, to_lang='ru'):

    def read_data():
        text = []

        with open(from_file, 'r', encoding='utf-8') as f:
            for i in f:
                print(i)
                text.append(i)
        return text

    def write_data(text):
        with open(text, 'w', encoding='utf-8') as translate:
            translate.write(text)

    params = {
        'key': API_KEY,
        'text': from_file,
        'lang': '{}-ru'.format(from_lng),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])
    json = translate_it('FR.txt', 'New_Translated', fr)


if __name__ == '__main__':
   pass
