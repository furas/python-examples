
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.16
#
# title: Append “N/A” doesnt work when there is no HTML element found by Beautifulsoup in python
# url: https://stackoverflow.com/questions/67998253/append-n-a-doesnt-work-when-there-is-no-html-element-found-by-beautifulsoup-in/68000492#68000492

import time
import random
import requests
from bs4 import BeautifulSoup 
import pandas as pd

df = pd.DataFrame({
    'keyword': ['lego 10934', 'lego 71372', 'lego 30556', 'lego 80106'],
    'sku': ['sku1', 'sku2', 'sku3', 'sku4'],
    'name': ['name1', 'name2', 'name3', 'name4'],
})

data_yeah   = []
data_lowest = []

for index, row in df.iterrows():
    #print(row)
    print('--- keyword:', row['keyword'], '---')
    
    time.sleep(random.randint(2, 6))
 
    url = "https://tw.mall.yahoo.com/search/product"

    payload = {
        'disp': 'list',
        'p': row['keyword'],
        'sort': 'p'
    }

    r = requests.get(url, params=payload)
    print('url:', r.url)
    
    soup = BeautifulSoup(r.text, 'html.parser')

    all_products = soup.find_all("div", {"class": "ListItem_mShop_33fil"})
    print('len(all_products):', len(all_products))

    try:
        yeah = soup.find("a", {"class": "ListItem_title_3CH7e textEllipsisLine2"}).string
    except:
        yeah = 'N/A'

    print('yeah:', yeah)
    data_yeah.append(yeah)
      
    try:        
        price = soup.find("div", {"class":"ListItem_price_2CMKZ"})
        lowest = price.find("span",{"class":"ListItem_priceContent_5WbI9"}).string
    except:
        lowest = "N/A"

    print('lowest:', lowest)
    data_lowest.append(lowest)

print('--- data ---')
print(data_yeah)
print(data_lowest)

df["Lowest Price in Yahoo Marketplace"] = data_lowest 
df["Competitor Product Name"] = data_yeah
df.to_excel("output.xlsx")
