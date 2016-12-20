#!/usr/bin/env python3

'''
Display data send as gzip

pip install requests
'''

import requests

url = 'http://www.stream-urls.de/webradio'

r = requests.get(url)

print('--- HEADERS ---')

print('Content-Type     :', r.headers['Content-Type'])      # gzip
print('Content-Encoding :', r.headers['Content-Encoding'])  # text/html; charset=utf-8

print('--- HTML ---')

#html = r.content # bytes - need decode('utf-8') (or similar)
html = r.text     # unicode - doesn't need decode()

print(html[:250], '...')
