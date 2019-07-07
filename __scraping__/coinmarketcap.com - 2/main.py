
# date: 2019.05.09
# author: Bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/56059703/how-can-i-make-lxml-save-two-pages-to-the-pages-so-it-can-be-read-by-the-tree

from lxml import html
import requests

data = {
    'BTC': 'id-bitcoin',
    'TRX': 'id-tron',
    # ...
    'HC': 'id-hypercash',
    'XZC': 'id-zcoin',
}

all_results = {}

for url in ('https://coinmarketcap.com/', 'https://coinmarketcap.com/2'):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    print(tree.cssselect('body'))
    for key, val in data.items():
        result = tree.xpath('//*[@id="' + val + '"]/td[4]/a/text()')
        print(key, result)
        if result:
            all_results[key] = result[0]

print('---')
print(all_results)
