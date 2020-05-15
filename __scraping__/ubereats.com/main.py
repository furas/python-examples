#!/usr/bin/env python3

# date: 2020.05.08
# https://stackoverflow.com/questions/61673305/requests-scrap-of-url-returns-404-even-with-headers-and-page-definitely-exists/

# this page needs header `Accept` 

from bs4 import BeautifulSoup
import requests

headers = {
#    'User-Agent': 'Mozilla/5.0',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#    "Accept-Encoding":"gzip, deflate, br"
#    "Accept-Language":"en-US;q=0.7,en;q=0.3"
}

url = 'https://www.ubereats.com/ann-arbor/food-delivery/chipotle-mexican-grill-3354-washtenaw-ave-ste-a/zbEbQIdWT2-n6iTWqjz55Q'
page = requests.get(url, headers=headers)

print(page.status_code)
print(page.text)
