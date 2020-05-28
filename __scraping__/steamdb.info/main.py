#!/usr/bin/env python3

# date: 2020.05.17

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
}

result = requests.get("https://steamdb.info/upcoming/free/", headers=headers)
soup = BeautifulSoup(result.content, 'lxml')

#print(result.content)
urls = []
for td_tag in soup.find_all('td'):
    a_tag = td_tag.find('a')
    if a_tag:
        urls.append(a_tag.attrs['href'])

print(urls)
