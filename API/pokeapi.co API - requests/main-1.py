# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.06
# [python - Please help extract the Pokemon names only from PokeAPI - Stack Overflow](https://stackoverflow.com/questions/71366959/please-help-extract-the-pokemon-names-only-from-pokeapi/71367645#71367645)
#
# https://pokeapi.co/docs/v2#pokemon

import requests
import pprint as pp

name_or_id = "stench"  # name
#name_or_id = 1         # id

url = "https://pokeapi.co/api/v2/ability/{}/".format(name_or_id)

response = requests.get(url)

if response.status_code != 200: 
    print(response.text)
else:
    data = response.json()
    #pp.pprint(data)
    
    print('\n--- data.keys() ---\n')
    print(data.keys())
    
    print('\n--- data["name"] ---\n')
    print(data['name'])

    print('\n--- data["names"] ---\n')
    pp.pprint(data["names"])
    
    print('\n--- data["names"][0]["name"] ---\n')
    print(data['names'][0]['name'])
    
    print('\n--- language : name ---\n')
    names = []
    for item in data["names"]:
        print(item['language']['name'],":", item["name"])
        names.append( item["name"] )
        
    print('\n--- after for-loop ---\n')
    print(names)

