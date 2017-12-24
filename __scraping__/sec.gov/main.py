
#
# https://stackoverflow.com/a/47742578/1832058
# https://stackoverflow.com/a/47614478/1832058
#

import requests
from bs4 import BeautifulSoup
import re


url = 'https://www.sec.gov/Archives/edgar/data/320193/000119312515356351/d17062d10k.htm'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')# "lxml")

# get all `b` to find title
all_b = soup.find_all('b')
for item in all_b:
    # check text in every `b`
    title = item.get_text(strip=True)
    if title == 'CONSOLIDATED BALANCE SHEETS':
        print('title >', title)
        # get first `table` after `b`
        table = item.parent.findNext('table')
        # all rows in table
        all_tr = table.find_all('tr')
        for tr in all_tr:
            # all columns in row
            all_td = tr.find_all('td')
            # text in first column
            text = all_td[0].get_text(strip=True)
            if text == 'Total assets':
                print('row >', text)
                for i, td in enumerate(all_td):
                    print('column', i, '>', td.get_text(strip=True))
