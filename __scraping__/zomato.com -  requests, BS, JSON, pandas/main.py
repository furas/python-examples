# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.08.12
# [python - Transforming Json File onto SQl Server - Stack Overflow](https://stackoverflow.com/questions/73332229/transforming-json-file-onto-sql-server/)

import json
from time import sleep
from random import randint

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from sqlalchemy import create_engine

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

all_items = []

for page in range(1, 3):
    print(f'--- page: {page} ---')

    url = f'https://www.zomato.com/beirut/deek-duke-ashrafieh/reviews?page={page}&sort=dd&filter=reviews-dd'
    response = requests.get(url ,headers=headers)
    soup = bs(response.text, 'html.parser')

    for tag in soup.find_all('script')[1]:
        item = tag[1454:-2]
        all_items.append(item)
        print(item)
        print('--------')

    sleep(randint(2,10))

# --- after loop ---

output = '[' + ',\n'.join(all_items) + ']'

data = json.loads(output)

df = pd.DataFrame(data)
df = df.join(df['reviewRating'].apply(pd.Series))
df = df.drop(columns='reviewRating')

print(df.to_string())
print(df.columns)

engine = create_engine("sqlite:///my_data.db")
#df.to_sql("table_name", con=engine, if_exists='replace')
df.to_sql("table_name", con=engine, if_exists='append') 

