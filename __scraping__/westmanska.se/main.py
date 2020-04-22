#!/usr/bin/env python3

# date: 2020.03.05
# https://stackoverflow.com/questions/60548952/python-beautifulsoup-find-between-tags/

import requests
from bs4 import BeautifulSoup

url = 'https://westmanska.se/dagens-lunch/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for row in soup.find('h1').find_next_siblings('p'):
    print(row.text)
