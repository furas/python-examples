#!/usr/bin/env python3 

# date: 2019.11.21
# https://stackoverflow.com/questions/58964487/beautifulsoup-scraping-other-pages-if-there-is-no-change-in-link-or-href-avail

import requests

headers = {
    'X-Api-Key': 'web-e3d812bf-d7a2-445d-ab38-55589ae6a121'
}

url = 'https://booksy.com/api/pl/2/customer_api/businesses/17101/reviews?reviews_page={}&reviews_per_page=5'

for x in range(1, 6):
    print('--- page:', x, '---')

    r = requests.get(url.format(x), headers=headers)
    data = r.json()

    for item in data['reviews']:
        print(item['user']['first_name'])
        print('>', item['review'])
        print('---')
        

