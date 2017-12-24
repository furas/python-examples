
#
# https://stackoverflow.com/a/47753174/1832058
# 

import requests

params = {
    'q': 'iot',
    'page': '1',
    'app': '',
    'sort': 'default',
    'ignoreSpellSuggestion': 'false',
}

url = 'https://www.mckinsey.com/services/ContentAPI/SearchAPI.svc/search'

for page in range(1, 3):

    params['page'] = str(page)

    r = requests.post(url, json=params)

    data = r.json() 

    print()
    print("data['data'].keys():\n", data['data'].keys())
    print()      
    print(' currentPage:', data['data']['currentPage'])
    print('  totalPages:', data['data']['totalPages'])
    print('totalResults:', data['data']['totalResults'])
    print()

    print("data['data']['results'][0].keys():\n", data['data']['results'][0].keys())
    print()

    for item in data['data']['results']:
        print(item['title'])
        print(item['url'])
        print('---')
