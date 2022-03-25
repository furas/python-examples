# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.24
# 

import requests
from bs4 import BeautifulSoup as BS

# this page need User-Agent
headers = { 
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0', 
}

url = 'https://www.the-numbers.com/movie/Avengers-Endgame-(2019)#tab=cast-and-crew'

r = requests.get(url, headers=headers)

# --- response ---

print(r.status_code)
#print(r.text[:1000])

soup = BS(r.text, 'html.parser')

all_items = soup.find_all('div', id="cast-and-crew") 
for item in all_items:
    print(item.get_text(strip=True, separator='\n'))

