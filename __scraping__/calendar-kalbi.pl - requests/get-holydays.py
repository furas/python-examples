#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as BS
import pprint
import json

data = {}

year = 2017
url = 'http://www.kalbi.pl/kalendarz-{}'.format(year)

r = requests.get(url)

soup = BS(r.text)

for m, month in enumerate(soup.select('td.yearCal_ym'), 1):
    data[m] = {}
    print('---', m, '---')

    print('- free -')
    for x in month.select('td.yearCal_free a'):
        d = int(x.text.strip())
        t = x.get('title').split('<br />')
        print('{:02d}.{:02d} {}'.format(m, d, t))
        if d not in data[m]:
            data[m][d] = {}
        data[m][d]['free'] = t

    print('- other -')
    for x in month.select('td.yearCal_nonfree a'):
        d = int(x.text.strip())
        t = x.get('title').split('<br />')
        print('{:02d}.{:02d} {}'.format(m, d, t))
        if d not in data[m]:
            data[m][d] = {}
        data[m][d]['other'] = t

# ---

pprint.pprint(data)

with open('{}-holydays.json'.format(year), 'w') as f:
    print(json.dumps(data))
    json.dump(data, f)
