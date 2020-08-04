
# author: https://blog.furas.pl
# date: 2020.07.31
# link: https://stackoverflow.com/questions/63180481/scraping-basketball-results-and-associate-related-competition-to-each-match/

import requests
import lxml.etree
from bs4 import BeautifulSoup as BS

url = 'http://www.nowgoal.group/GetNbaWithTimeZone.aspx?date=2020-07-29&timezone=2&kind=0&t=1596143185000'

r = requests.get(url)

# --- lxml ---

soup = lxml.etree.fromstring(r.content)

all_items = soup.xpath('//h')

for item in all_items:
    values = item.text.split('^')
    #print(values)
    print(values[8], values[11])
    print(values[10], values[12])
    print('---')

# --- BS ---

soup = BS(r.text, 'html.parser')

all_items = soup.find_all('h')

for item in all_items:
    values = item.text.split('^')
    #print(values)
    print(values[8], values[11])
    print(values[10], values[12])
    print('---')

