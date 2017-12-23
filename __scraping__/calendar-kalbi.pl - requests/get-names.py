#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as BS
import pprint
import json

data = {}

year = 2017

month_names = (
    'styczen', 'luty', 'marzec',
    'kwiecien', 'maj', 'czerwiec',
    'lipiec', 'sierpien', 'wrzesien',
    'pazdziernik', 'listopda', 'grudzien'
)

for m, month in enumerate(month_names, 1):

    url = 'http://www.kalbi.pl/kalendarz-imienin-{}-{}'.format(month, year)
    print('url:', url)

    r = requests.get(url)

    soup = BS(r.text, 'lxml')

    data[m] = {}

    d = 0
    for day in soup.select('td.calendar_d'):
        if 'calendar_dnp' not in day.get('class'):
            d += 1
            t = day.text.strip().split('  ')[1]
            data[m][d] = t.split(', ')

# ---

pprint.pprint(data)

with open('{}-names.json'.format(year), 'w') as f:
    print(json.dumps(data))
    json.dump(data, f)
