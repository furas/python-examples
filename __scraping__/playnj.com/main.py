#!/usr/bin/env python3

# date: 2020.01.10
# https://stackoverflow.com/questions/59682409/trouble-scraping-a-table-with-python-beautifulsoup/

import requests
from bs4 import BeautifulSoup

url = 'https://www.playnj.com/atlantic-city/revenue/'
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

october_table = soup.find('table', {'id': 'tablepress-342'})
#print(october_table)
for row in october_table.find_all('tr'):
    for item in row.find_all('td'):
        print(item.text)
    print('---')
