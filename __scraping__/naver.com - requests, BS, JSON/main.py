
# author: https://blog.furas.pl
# date: 2020.07.09
# https://stackoverflow.com/questions/62807158/python-beautifulsoup-get-html-from-dynamic-page/

import requests
from bs4 import BeautifulSoup
import json

# --- functions ---

def get_data(url):

    r = s.get(url, timeout=100)
    print(r.status_code)

    soup = BeautifulSoup(r.content, 'html.parser')
    script = soup.find('script', {'id': '__NEXT_DATA__'})

    data = json.loads(script.text)        
    products = data['props']['pageProps']['initialState']['products']['list']

    print('len(products):', len(products))

    for item in products:
        print('productName:', item['item']['productName'])
        for key, value in item['item'].items():
            print('   >', key, '=', value)

# --- main ---

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'})

# main page to get cookies
url = 'https://shopping.naver.com/'
r = s.get(url)

# search
query = 'test'

# I don't need it because I can get it with `pagingIndex=1`
url = 'https://search.shopping.naver.com/search/all?cat_id=&frm=NVSHATC&query={}'.format(query)
get_data(url)

# pages    
for page in range(1, 3):
    print('\n--- page', page, '---\n')
    
    url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=test&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(page, query)
    get_data(url)
    

