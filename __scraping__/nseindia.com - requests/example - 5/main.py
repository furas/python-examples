#!/usr/bin/env python3

# date: 2020.01.10
# https://stackoverflow.com/questions/59683802/unable-to-scrape-tabular-data-in-nse/

import requests

url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/changePercentage.json'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
data = r.json()
print(data['rows'][0]['advances'])
print(data['rows'][0]['declines'])
print(data['rows'][0]['unchanged'])
print(data['rows'][0]['total'])


