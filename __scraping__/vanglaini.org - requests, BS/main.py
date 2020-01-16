#!/usr/bin/env python3

# date: 2019.10.12

import requests
from bs4 import BeautifulSoup 
import pandas as pd

response = requests.get('https://www.vanglaini.org/')
soup = BeautifulSoup(response.text, 'lxml')

data = []

for article in soup.find_all('article'):
    if article.a is None:
        continue
    row = [
        article.a.text.strip(), # headline
        article.p.text.strip(), # summary
        "https://www.vanglaini.org" + article.a['href'] # link
    ]
    data.append(row)
    
df = pd.DataFrame(data, columns=['Headline', 'Summary', 'Link'])
print(df)
