# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.08.10
# [python - BeautifulSoup trying get info from next page - Stack Overflow](https://stackoverflow.com/questions/73298457/beautifulsoup-trying-get-info-from-next-page/)

#import random
#import time
import requests
import pandas as pd

def get_pages(pages, start=1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'catalogNodeId': 313,
        'pageNumber': 0
    }

    url = 'https://list.szlcsc.com/products/list'

    # --- before loop ---

    all_products = []

    # --- loop ---

    for page in range(start, start+pages):
        print('page:', page)

        params['pageNumber'] = page

        response = requests.post(url, headers=headers, data=params)
        data = response.json()

        all_products += data['productRecordList']

        #time.sleep(random.randint(3, 10))  # to behave like real human

    # --- after loop ---

    return pd.DataFrame(all_products)

# --- main ---

df = get_pages(3)

df['productId'] = df['productId'].astype(int)

print(df[['productId', 'productName', 'totalStockNumber']].sort_values('productId'))

