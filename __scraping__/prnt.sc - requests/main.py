
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.07
#
# title: Image source is different in html between my browser and get request
# url: https://stackoverflow.com/questions/69474455/image-source-is-different-in-html-between-my-browser-and-get-request/69475459#69475459

# [Image source is different in html between my browser and get request](https://stackoverflow.com/questions/69474455/image-source-is-different-in-html-between-my-browser-and-get-request/69475459#69475459)

import requests
from lxml import html

url = "https://prnt.sc/ca0000"

response = requests.get(url, headers={'User-Agent': 'Chrome'})

tree = html.fromstring(response.content)

image_url = tree.xpath('//img[@id="screenshot-image"]/@src')[0]

print(image_url)

response = requests.get(image_url, headers={'User-Agent': 'Chrome'})

with open('image.png', 'wb') as fh:
    fh.write(response.content)
