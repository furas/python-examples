# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.06
# [python - Please help extract the Pokemon names only from PokeAPI - Stack Overflow](https://stackoverflow.com/questions/71366959/please-help-extract-the-pokemon-names-only-from-pokeapi/71367645#71367645)
#
# https://pokeapi.co/docs/v2#pokemon

import requests
import pprint as pp

url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

for offset in range(0, 1000, 100):

    params['offset'] = offset  # add new value to dict with `limit`

    response = requests.get(url, params=params)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        #pp.pprint(data)

        for item in data['results']:
            print(item['name'])

