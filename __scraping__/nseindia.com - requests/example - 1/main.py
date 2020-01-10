#!/usr/bin/env python3

# date: 2019.04.22
# https://stackoverflow.com/questions/55788117/how-scrape-a-website-in-which-i-post-information/

import requests
#import json
import dirtyjson

url = 'https://nseindia.com/corporates/corpInfo/equities/getAnnouncements.jsp?period=Latest%20Announced'

r = requests.get(url)
#data = r.json() # doesn't work because JSON data has some mistakes

#text = r.text.strip()
#print(text)
#data = json.loads(text) # doesn't work because JSON data has some mistakes

data = dirtyjson.loads(r.text)
#print(data)

for item in data['rows']:
    #print(item)
    print(item.keys())
    print(item['sym'])
    print(item['desc'])
    print(item['name'])
    print(item['date'][:2], item['date'][2:4], item['date'][4:8])
