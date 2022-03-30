# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.29
# [python - How do I parse all the 400 francises from this website if pages 2, 3, 4 all have the same URL? - Stack Overflow](https://stackoverflow.com/questions/71668453/how-do-i-parse-all-the-400-francises-from-this-website-if-pages-2-3-4-all-have/)

import requests

payload = {
    'bl': '1111254',
    'o': 0,
    'l': 25,    # 'l':400 to get all in one request
    'f': 'json',
    'altf': 'widget',
}

url = 'https://www.franchisetimes.com/search/'

for offset in range(0, 400, 25):
    print('\n--- offset:', offset, '---\n')
    
    payload['o'] = offset
    response = requests.get(url, params=payload)
    data = response.json()
    for item in data['assets']:
        print('rank :', item["rank"])
        print('title:', item['title'])
        print('name :', item["name"])
        print('sales:', item["sales"])
        print('loc  :', item["loc"])
        print('logo :', item["preview"]["url"])
        print('---')
        
