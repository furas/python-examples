# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.21
# 

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
  
URL = "https://www.ubereats.com/location"

req = Request(URL, headers={'User-Agent': 'Chrome/103.0.5060.114', 'Accept': 'text/html,application/xhtml+xml,application/xml'})
webpage = urlopen(req).read()
# print(webpage)
soup = BeautifulSoup(webpage, 'html.parser') 

#Fetching URL of all cities
states = soup.select("h2 a")
states = [state for state in states if state.text != "All Countries"]
print('states:', len(states))

rows = []
for state in states:
    print(f"Processing: {state.text}")
    cities = state.parent.parent.parent.select("a span")
    print('cities:', len(cities))
    for city in cities:
        rows.append([
            city.text,
            state.text,
            "https://www.ubereats.com" + city.parent['href']
        ])
        
# ---

import pandas as pd

df = pd.DataFrame(rows, columns=['city', 'state', 'url'])

print(df)

