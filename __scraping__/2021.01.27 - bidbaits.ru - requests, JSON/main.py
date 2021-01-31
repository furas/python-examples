
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.01.27

# Website's search function with Python requests
# https://stackoverflow.com/questions/65920704/websites-search-function-with-python-requests/

import requests

headers = {
    #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    #'Accept': 'application/json, text/javascript, */*; q=0.01',
    #'X-Requested-With': 'XMLHttpRequest',  # AJAX
    'Referer': 'https://bidbaits.ru/',
}

url = 'https://bidbaits.ru/searchresults/?page=1&seo=SEARCH&orderBy=2&used=1&new=1&original=1&replica=1&auctions=1&fixedPrice=1&discount=0&trustedSeller=0&lockLocation=0&q=cyarl&c=0'
r = requests.get(url, headers=headers)

data = r.json() 
#print(data)

#import json
#print(json.dumps(data, indent=2))

for item in data['items']:
    print('name:', item['name'])
    print('price:', item['price'])    
    print('---')
