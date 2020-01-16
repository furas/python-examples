#!/usr/bin/env python3

# date: 2020.01.13
# https://stackoverflow.com/questions/59710076/encode-unicode-characters-in-dict-to-send-as-data-in-a-post-request/

# page uses ISO-8859-1 

import requests
import urllib.parse
import webbrowser

d = {
    'fromClass': 'Golfito',
    'toClass': 'Cañon del Guarco',
    'viaClass': '',
    'jDate': '01/12/2020',
    'jTime': '21:34',
    'addtime': '0',
    'lang': 'en',
    'b2': 'Search connection'
}

d = urllib.parse.urlencode(d, encoding='ISO-8859-1')
h = {'Content-Type': 'application/x-www-form-urlencoded'}
#print(d)

r = requests.post('http://horariodebuses.com/EN/cr/index.php', data=d, headers=h)

#print(r.encoding)
#print(r.request.body)
#print(r.request.headers)

with open('output.html', 'wb') as f:
    f.write(r.content)
webbrowser.open('output.html')
