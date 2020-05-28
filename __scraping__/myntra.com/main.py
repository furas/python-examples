#!/usr/bin/env python3

# date: 2020.03.05
# https://stackoverflow.com/questions/60547578/extract-data-from-script-tag/

import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.myntra.com/men-formal-shirts?f=Collar%3AButton-Down%20Collar"
base_url = "https://www.myntra.com/men-footwear"

r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')

# get .text
scripts = soup.find_all('script')[8].text

# remove window.__myx = 
script = scripts.split('=', 1)[1]

# convert to dictionary
data = json.loads(script)

for item in data['searchData']['results']['products'][:3]:
    #print(item.keys())
    #for key, value in item.items():
    #    print(key, '=', value)
    
    print('product:', item['product'])
    print('productId:', item['productId'])
    print('brand:', item['brand'])
    print('url:', 'https://www.myntra.com/men-footwear/' + item['landingPageUrl'])
    print('---')
