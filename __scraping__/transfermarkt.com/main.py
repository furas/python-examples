
# date: 2019.05.05
# author: Bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/55992681/how-to-scrape-a-website-table-where-the-cell-values-have-the-same-class-name

import requests
from bs4 import BeautifulSoup
import pandas as pd


data = {
    'name': [],
    'data of birth': [],
    'height': [],
    'foot': [],
    'joined': [],
    'contract until': [],
}

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}

url = "https://www.transfermarkt.com/hertha-bsc-u17/kader/verein/21066/saison_id/2018/plus/1"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

all_tr = soup.find_all('tr', {'class': ['odd', 'even']})
#print('rows:', len(all_tr))

for row in all_tr:
    all_td = row.find_all('td', recursive=False)

    #print('columns:', len(all_td))
    #for column in all_td:
    #    print(' >', column.text)

    data['name'].append( all_td[1].text.split('.')[0][:-1] )
    data['data of birth'].append( all_td[2].text[:-5] )
    data['height'].append( all_td[4].text )
    data['foot'].append( all_td[5].text )
    data['joined'].append( all_td[6].text )
    data['contract until'].append( all_td[8].text )

df = pd.DataFrame(data)
print(df.head())
