#!/usr/bin/env python3

# date: 2020.02.26
# https://stackoverflow.com/questions/60408917/how-to-scrape-data-from-different-wikipedia-pages/

import requests
from bs4 import BeautifulSoup as BS
import re

def parse_district(url):
    r = requests.get(url)

    soup = BS(r.text, 'html.parser')

    link = soup.find('a', {'href': re.compile('//tools.wmflabs.org/.*')})

    item = link['href'].split('params=')[1].split('type:')[0].replace('_', ' ').strip()
    #print(item)

    items = link.find_all('span', {'class':('latitude', 'longitude')})

    #print('>>>', [item] + [i.text for i in items][:3] )

    return [item] + [i.text for i in items]

def main():
    url = 'https://en.wikipedia.org/wiki/Districts_of_Hong_Kong'

    r = requests.get(url)

    soup = BS(r.text, 'html.parser')

    table = soup.find_all('table', {'class': 'wikitable'})
    for row in table[0].find_all('tr'):
        items = row.find_all('td')
        if items:
            row = [i.text.strip() for i in items]

            link = 'https://en.wikipedia.org' + items[0].a['href']
            data = parse_district(link)

            row += data
            print(row)
main()   
