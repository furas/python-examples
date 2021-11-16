
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.16
#
# title: Python unable to get API with requests: Web scraping, Requests, API
# url: https://stackoverflow.com/questions/69982326/python-unable-to-get-api-with-requests-web-scraping-requests-api/69992299#69992299

# [Python unable to get API with requests: Web scraping, Requests, API](https://stackoverflow.com/questions/69982326/python-unable-to-get-api-with-requests-web-scraping-requests-api/69992299#69992299)

import requests

url = 'https://www.atacadao.com.br/catalogo/search/?q=&category_id=null&category[]=bebidas&page=1&order_by=-relevance'

url = 'https://www.atacadao.com.br/catalogo/search/'

payload = {
    'q': '',
    'category_id': 'null',
    'category[]': 'bebidas',
    'page': 1,
    'order_by': '-relevance'
}

# ---

for number in range(1, 6):

    print('\n=== page:', number, '===\n')
    
    payload['page'] = number
    
    r = requests.get(url, params=payload)
    #print(r.text[:1000])   # show only beginning of data

    data = r.json()

    for item in data['results'][:3]:   # show only first three results
        #print(item.keys())
        print('name:', item['name'])
        print('price:', item['price'])
        print('url:', item['url'])
        print('---')
        
# --- the same with `while True` loop

number = "1"

while True:

    print('\n=== page:', number, '===\n')
    
    payload['page'] = number
    
    r = requests.get(url, params=payload)
    #print(r.text[:1000])   # show only beginning of data

    data = r.json()

    for item in data['results'][:3]:   # show only first three results
        #print(item.keys())
        print('name:', item['name'])
        print('price:', item['price'])
        print('url:', item['url'])
        print('---')
        
    number = data['pagination']['next']
    
    if not number:
        break

# or 

number = "1"

while number:

    print('\n=== page:', number, '===\n')
    
    payload['page'] = number
    
    r = requests.get(url, params=payload)
    #print(r.text[:1000])   # show only beginning of data

    data = r.json()

    for item in data['results'][:3]:   # show only first three results
        #print(item.keys())
        print('name:', item['name'])
        print('price:', item['price'])
        print('url:', item['url'])
        print('---')
        
    number = data['pagination']['next']

