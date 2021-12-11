
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.11
#
# title: Getting duplicate links for images in scraping with BeautifulSoup
# url: https://stackoverflow.com/questions/70314063/getting-duplicate-links-for-images-in-scraping-with-beautifulsoup/70314137?noredirect=1#comment124295605_70314137

# [Getting duplicate links for images in scraping with BeautifulSoup](https://stackoverflow.com/questions/70314063/getting-duplicate-links-for-images-in-scraping-with-beautifulsoup/70314137?noredirect=1#comment124295605_70314137)

import requests
from bs4 import BeautifulSoup

testlink = 'https://trgovina.audiopro.si/si/bas-glave/36037-81020104.html'

r = requests.get(testlink)
soup = BeautifulSoup(r.content, 'html.parser')

imagelinks = []

name = soup.find('h1', class_='product_name').text.strip()

reference = soup.find('div', class_='product-reference_top product-reference')
reference_number = reference.find('span').text
print(reference_number)

#images = soup.find('div', {'id':'thumb_box'}).find_all('li', class_='thumb-container')
images = soup.select('div#thumb_box li.thumb-container')

for item in images:
    image = item.find('img').attrs['src']
    imagelinks.append(image)

print(imagelinks)
print(len(imagelinks))

