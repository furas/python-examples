
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.16
#
# title: Python unable to get API with requests: Web scraping, Requests, API
# url: https://stackoverflow.com/questions/69982326/python-unable-to-get-api-with-requests-web-scraping-requests-api/69992299#69992299

# [Python unable to get API with requests: Web scraping, Requests, API](https://stackoverflow.com/questions/69982326/python-unable-to-get-api-with-requests-web-scraping-requests-api/69992299#69992299)

import requests

url = 'https://www.atacadao.com.br/catalogo/search/?q=&category_id=null&category[]=bebidas&page=1&order_by=-relevance'

r = requests.get(url)

print(r.text[:1000])   # show only beginning of data
print('------------')

data = r.json()

for item in data['results'][:3]:   # show only first three results

    #print(item.keys())

    #for key, val in item.items():
    #    print(f'{key}: {val}')

    print('name:', item['name'])
    print('price:', item['price'])
    print('url:', item['url'])

    print('---')
    
