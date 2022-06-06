# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.06
# [python - How do web scrape more underlying data from a websites map location? - Stack Overflow](https://stackoverflow.com/questions/72519666/how-do-web-scrape-more-underlying-data-from-a-websites-map-location/72519894#72519894)

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
}

url = 'https://www.homedepot.com/StoreSearchServices/v2/storesearch'

payload = {
    'address': 37028,
    'radius': 250,
    'pagesize': 40,
    'page': 1,
}

page = 0

while True:

    page += 1
    print('--- page:', page, '---')
    
    payload['page'] = page
    response = requests.get(url, params=payload, headers=headers)
    
    data = response.json()

    print(data['searchReport'])
                        
    if "stores" not in data:
        break
    
    for number, item in enumerate(data['stores'], 1):
        print(f'{number:2} | phone: {item["phone"]} | zip: {item["address"]["postalCode"]}')

