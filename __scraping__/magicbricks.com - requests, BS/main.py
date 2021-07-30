
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.15
#
# title: How to scrap string that does not have unique ID for data extraction? [closed]
# url: https://stackoverflow.com/questions/68394176/how-to-scrap-string-that-does-not-have-unique-id-for-data-extraction

from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.magicbricks.com/property-for-sale-in-namakkal-pppfs'
r= requests.get(url)

soup = BS(r.text, 'html.parser')

all_items = soup.find_all('span', class_='m-srp-card__title')
for item in all_items:
    print('for Sale in', item.text.split('for Sale in')[1].strip() )

