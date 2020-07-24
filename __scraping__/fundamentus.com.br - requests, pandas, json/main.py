
# author: https://blog.furas.pl
# date: 2020.07.16
# link: https://stackoverflow.com/questions/62921395/pandas-include-key-to-json-file/

import requests
import pandas as pd
import json

url = 'http://www.fundamentus.com.br/resultado.php'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

response = requests.get(url, headers=headers)

dfs = pd.read_html(response.text)
table = dfs[0]
table.to_json('table7.json', orient='records', indent=2)

jasonfile = open('table7.json', 'r')
stocks = jasonfile.read()
jason_object = json.loads(stocks)

#print(jason_object[0]['Papel'])

#for key in jason_object[0].keys():
#    print(key)

new_data = dict()

for item in jason_object:
    key = item['Papel']
    item.pop('Papel')
    val = item
    new_data[key] = val

print(new_data)

