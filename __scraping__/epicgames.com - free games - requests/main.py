#!/usr/bin/env python3

# date: 2020.05.18
# https://stackoverflow.com/questions/61876744/scraper-returns-null-result/

import requests

url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=PL&allowCountries=PL'

r = requests.get(url)

data = r.json()

#print(r.text)

for item in data['data']['Catalog']['searchStore']['elements']:
    print(item['title'])
    offers = item['promotions']['promotionalOffers']
    for offer in offers:
        print(offer['promotionalOffers'][0]['startDate'])
        print(offer['promotionalOffers'][0]['endDate'])

