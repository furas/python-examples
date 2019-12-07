#!/usr/bin/env python3 

# date: 2019.12.05
# 

import urllib.request
import brotli

url = 'https://sports.coral.co.uk/sport/football/matches/tomorrow'

r = urllib.request.urlopen(url)
html = r.read()
r.close()

print('--- HEADERS ---')
print('Content-Type    :', r.headers['Content-Type'])     # text/html
print('Content-Encoding:', r.headers['Content-Encoding']) # br

print('--- HTML ---')
print('before:', html[:10])
html = brotli.decompress(html)
print(' after:', html[:10])
