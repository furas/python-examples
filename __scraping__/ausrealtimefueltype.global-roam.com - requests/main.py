#!/usr/bin/env python3

# date: 2020.01.17
# https://stackoverflow.com/questions/59779978/python-requests-output-is-different-to-expected-output/

import requests

headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://ausrealtimefueltype.global-roam.com/api/SeriesSnapshot?time='

r = requests.get(url,  headers=headers)
data = r.json()

for item in data['seriesCollection']:
    #for key, value in item.items():
    #    print(key, value)
    print('region:', item['metadata']['region']['name'])
    print('fuel type:', item['metadata']['fuelType']['name'])
    print('value:', item['value'])
    print('---')

