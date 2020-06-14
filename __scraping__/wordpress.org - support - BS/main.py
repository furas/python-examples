#!/usr/bin/env python3

# date: 2020.06.14
# https://stackoverflow.com/questions/62373373/bs4-fetching-thread-titles-description-plus-more-from-wordpress-org-support-fo

import requests
from bs4 import BeautifulSoup as BS

url = 'https://wordpress.org/support/plugin/advanced-gutenberg/page/{}/'
headers = {'user-agent': 'Mozilla/5.0'}

for page in range(1, 6):
    print('---', page, '---')

    # this page need header `user-agent`
    r = requests.get(url.format(page), headers=headers)

    soup = BS(r.text, 'html.parser')
    
    for ul in soup.find('li', class_="bbp-body").find_all('ul'):
        a = ul.find('a')
        if a:
            print('text:', a.text)
            print('href:', a['href'])
        print('-')
