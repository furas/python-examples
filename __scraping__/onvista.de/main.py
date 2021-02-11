# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.11
# link: (stackoverflow) https://stackoverflow.com/questions/66154423/concanate-class-str-array-to-dataframe

import pandas as pd
import requests

headers = {'User-Agent': 'Chrome/70.0.3538.110'}  # PEP8: spaces around `=`

payload = {
     'continent[0]': 'Europa',
     'continent[1]': 'Nordamerika',
     'continent[2]': 'Asien - Pazifik',
     'PROFIT_PER_SHARE[enabled]': 1, 
     'PROFIT_KGV[enabled]': 1,
     'MARKET_CAPITALIZATION[enabled]': 1,
     'PERFORMANCE_6_MONTHS[enabled]': 1,
     'PERFORMANCE_4_WEEKS[enabled]': 1,
     'SCREENER_INTEREST[enabled]': 1,
     'SCREENER_RISK_ZONE[enabled]': 1,
     'PROFIT_PER_SHARE[year]': 2020,
     'PROFIT_KGV[year]': 2020,
     'MARKET_CAPITALIZATION[year]': 2020,
     'offset': 0,
}

url = 'https://www.onvista.de/aktien/finder/'

table_dfs = []  # list

for offset in range(0, 3*50, 50):

    payload['offset'] = offset

    response = requests.get(url, params=payload, headers=headers)
 
    all_tables = pd.read_html(response.text)
    table_dfs.append( all_tables[0] )  # `[0]` - first DataFrame from list
    
    #print(type(all_tables), all_tables)
    #print(type(all_tables[0]), all_tables[0])
    
df = pd.concat(table_dfs, ignore_index=True)

print(len(df))
print(df)
