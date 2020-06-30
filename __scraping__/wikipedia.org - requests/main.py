
# date: 2019.07.19
# https://stackoverflow.com/questions/57107634/python-extract-information-from-html

# https://2.python-requests.org/en/master/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup as BS

url = 'https://en.wikipedia.org/wiki/Microsoft'

r = requests.get(url)

soup = BS(r.text, 'html.parser')

all_tables = soup.find_all('table')

all_rows = all_tables[0].find_all('tr')
for row in all_rows:

    th = row.find('th')
    if not th:
        continue
    
    title = th.text
       
    td = row.find('td')
    all_li = td.find_all('li')

    if all_li:
        for item in all_li:
            print(title, '>', item.get_text())
    else:
        print(title, '>', td.get_text())
 
