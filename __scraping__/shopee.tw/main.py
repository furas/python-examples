#!/usr/bin/env python3

# date: 2020.01.02
# https://stackoverflow.com/questions/59557071/how-can-i-crawl-the-product-items-from-shopee-website/59557626#59557626

# Without `Referer` it doesn't send price

import requests

url = 'https://shopee.tw/api/v2/search_items/?by=pop&limit=30&match_id=1819984&newest=0&order=desc&page_type=shop&shop_categoryids=9271157&version=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Referer': 'https://shopee.tw/shop/1819984/search?shopCollection=9271157',
    'X-Requested-With': 'XMLHttpRequest',
}    

r = requests.get(url, headers=headers)

data = r.json()

#print(data['items'][0].keys())

for item in data['items']:
    print('name:', item['name'])
    print('prince:', item['price'])
    print('---')
