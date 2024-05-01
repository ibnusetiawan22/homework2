import requests

api_key = '010d314c-2e39-416f-aa11-21814b1ddd68'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

# Lakukan permintaan HTTP dan simpan respons dalam variabel res
res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
