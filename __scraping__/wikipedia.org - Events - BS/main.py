#!/usr/bin/env python3

# date: 2020.06.17
# https://stackoverflow.com/questions/62420416/web-scraping-with-bs4-how-to-set-a-range-of-where-to-look/

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/2020')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

# found start of data `h2`
start = soup.find('span', {'id': 'Events'}).parent

# check sibling items
for item in start.next_siblings:

    # found end of data `h2`
    if item.name == 'h2': 
        break

    if item.name == 'ul':

        # only direct `li` without nested `li`
        for li in item.find_all('li', recursive=False): 

            # `a` which have `title`
            a = li.find('a', {'title': True}) 

            if a:
                print(a['title'])
                
