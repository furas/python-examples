#!/usr/bin/env python3

# date: 2020.03.03
# https://stackoverflow.com/questions/60505000/python-lxml-cant-parse-japanese-in-some-case/
# python lxml can't parse japanese in some case 
# https://stackoverflow.com/questions/44203397/python-requests-get-returns-improperly-decoded-text-instead-of-utf-8
# python requests.get() returns improperly decoded text instead of UTF-8?


import requests
import lxml.html
import chardet

chrome_ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 " \
            "(KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36"

with requests.Session() as s:
    s.headers.update({'User-Agent': chrome_ua})
    resp = s.get('https://travel.rakuten.co.jp/')

print('encoding:', resp.encoding)
print('apparent:', resp.apparent_encoding)
print('chardet :', chardet.detect(resp.content) )

tree = lxml.html.fromstring(resp.text)
result = tree.xpath('//*[@id="rt-nav-box"]/li[1]/a')[0]
print(result.text)

detected_encoding = chardet.detect(resp.content)['encoding']
html = resp.content.decode(detected_encoding)
tree = lxml.html.fromstring(html)
result = tree.xpath('//*[@id="rt-nav-box"]/li[1]/a')[0]
print(result.text)

resp.encoding = resp.apparent_encoding
tree = lxml.html.fromstring(resp.text)
result = tree.xpath('//*[@id="rt-nav-box"]/li[1]/a')[0]
print(result.text)

