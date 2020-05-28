
# date: 2020.05.26
# https://stackoverflow.com/questions/61994836/bs4-web-scraping-searching-div-class/

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
r = requests.get('https://www.google.com/search?q=titanic+movie', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
item = soup.find('div', class_="srBp4 Vrkhme")
print(item.get_text(strip=True, separator=' '))

