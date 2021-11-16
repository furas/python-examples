
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.05
#
# title: Python Trouble Downloading excel file with Dynamic Url with No extension
# url: https://stackoverflow.com/questions/69847923/python-trouble-downloading-excel-file-with-dynamic-url-with-no-extension/69848101#69848101

# [Python Trouble Downloading excel file with Dynamic Url with No extension](https://stackoverflow.com/questions/69847923/python-trouble-downloading-excel-file-with-dynamic-url-with-no-extension/69848101#69848101)

import requests
from bs4 import BeautifulSoup

url = 'https://www.djppr.kemenkeu.go.id/page/loadViewer?idViewer=9369&action=download'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

src = soup.find('iframe')['src']
print(src)

url = 'https://www.djppr.kemenkeu.go.id' + src

r = requests.get(url)
with open('file.xlsx', 'wb') as f:
    f.write(r.content)
