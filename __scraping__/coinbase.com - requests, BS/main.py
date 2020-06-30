#!/usr/bin/env python3 

# date: 2019.12.02
# https://stackoverflow.com/questions/59132449/what-is-the-proper-syntax-for-find-in-bs4

import requests
from bs4 import BeautifulSoup

url = 'https://www.coinbase.com/charts'
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

all_tr = soup.find_all('tr')

data = []

for tr in all_tr:
    row = []
    for h4 in tr.find_all('h4'):
        row.append(h4.text)
    if row: # skip empty row
        data.append(row)

for row in data:
    print(row)

