
# date: 2020.08.25
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# link: (stackoverflow) https://stackoverflow.com/questions/63578552/having-trouble-interpreting-website-source-code/

import requests
from bs4 import BeautifulSoup

url = ' https://www.footywire.com/afl/footy/dream_team_breakevens'
search = 'Kennedy'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print('get rows')

all_rows = soup.find_all('tr', {'onmouseover': True})
#all_rows = soup.select('tr[onmouseover]')

for row in all_rows:
    print('get columns')
    
    all_cols = row.find_all('td')
    #all_cols = row.select('td')
    
    #for idx, item in enumerate(all_cols):
    #    print(idx, item.text)
    
    #name = all_cols[0].find('a').text
    name = all_cols[0].select_one('a').text
    breakeven = all_cols[5].text
    
    if search in name:
        print(name, breakeven)
        break # exit loop and don't check other rows
