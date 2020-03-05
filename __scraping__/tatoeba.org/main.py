#!/usr/bin/env python3

# date: 2020.02.24
# https://stackoverflow.com/questions/60372726/scraping-dictionary-entries-using-pythons-beautifulsoup/

from bs4 import BeautifulSoup #as BS
import requests
import json

word = "Verwirrung"
url = "https://tatoeba.org/eng/sentences/search?query={}&from=und&to=spa".format(word)
vstr = requests.get(url).content
Soup = BeautifulSoup(vstr, features="html.parser")

rows = Soup.findAll('div', {"class":"sentence-and-translations md-whiteframe-1dp"})

for row in rows:
    data = '[' + row['ng-init'][11:-1] + ']'
    #print(data)
    data = json.loads(data)
    #print(data[0].keys())
    print('DE:', data[0]['text']) #, data[0]['lang'], data[0]['langName'])
    for item in data[1]:
        print('ES:', item['text']) #, item['lang'], item['langName'])
    for item in data[2]:
        print('ES:', item['text']) #, item['lang'], item['langName'])
