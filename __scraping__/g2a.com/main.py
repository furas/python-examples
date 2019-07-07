
# date: 2019.05.19
# author: Bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56208824/403-forbidden-error-when-scraping-a-site-user-agents-already-used-and-updated?noredirect=1#comment99040341_56208824

import requests

url = 'https://www.g2a.com/lucene/search/filter?&search=The+Elder+Scrolls+V:+Skyrim&currency=nzd&cc=NZD'

headers = {
 #   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept-Language': 'en-US;q=0.7,en;q=0.3',
}

r = requests.get(url, headers=headers)

data = r.json()
print(data['docs'][0]['name'])
