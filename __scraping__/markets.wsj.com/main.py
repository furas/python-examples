
# date: 2019.04.10
# https://stackoverflow.com/questions/55604518/how-do-i-move-data-scraped-with-beautifulsoup-to-a-mysql-database/55604754#55604754

import urllib.request
from bs4 import BeautifulSoup

html_url = 'https://markets.wsj.com/'
html_doc = urllib.request.urlopen(html_url).read()

soup = BeautifulSoup(html_doc, 'html.parser')
markets = soup.find(id='majorStockIndexes_moduleId')

marketRows = markets.tbody.find_all('tr')

for row in marketRows:
    all_td = row.find_all('td')
    arguments = [x.text.strip() for x in all_td]
    print(arguments)
    # ... here INSERT data to database ...
