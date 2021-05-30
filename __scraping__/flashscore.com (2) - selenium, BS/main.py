
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.29
#
# title: Scraping a section of webpage based on text
# url: https://stackoverflow.com/questions/67754320/scraping-a-section-of-webpage-based-on-text/67756231#67756231

import selenium.webdriver
from bs4 import BeautifulSoup as BS
import time

url = 'https://www.flashscore.com/football/chile/primera-division/'

driver = selenium.webdriver.Firefox()
driver.get(url)

time.sleep(5)

soup = BS(driver.page_source, 'html.parser')

print('--- version 1 ---')

section = soup.find('div', id='live-table').find('section')

for item in section.find_all('div', title='Click for match detail!'):
    print(item.get('id'))

print('--- version 2 ---')

section = soup.find('section', class_='event--live')

for item in section.find_all('div', title='Click for match detail!'):
    print(item.get('id'))


