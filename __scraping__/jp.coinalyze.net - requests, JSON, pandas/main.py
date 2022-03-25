# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.18
# [web scraping - Structuring an XHR request with python to fetch chart data - Stack Overflow](https://stackoverflow.com/questions/71523031/structuring-an-xhr-request-with-python-to-fetch-chart-data/)

import requests
from pprint import pprint

s = requests.Session()

headers = {
#    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
}

url = "https://jp.coinalyze.net/chart/getBars/"

print('GET')
response = s.get(url, headers=headers)

data = {
    "from": 1647489482,
    "to": 1647585482,
    "resolution": "5",
    "symbol": "1000XECUSDT_PERP.A",
    "firstDataRequest": 'true',
    "symbolsForUsdConversion": [],
    "rk": "dd339ecf-1272-4b5a-a0ce-c3181bf7feac"
}

headers = {
#    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
#    'X-Requested-With': 'XMLHttpRequest',
#    'Referer': 'https://jp.coinalyze.net/1000xec/usdt/binance/1000xecusdt_perp/price-chart-live/',
}

print('POST')
response = s.post(url, json=data, headers=headers)
#pprint(response.text[:1000])

data = response.json()
#pprint(data)

import pandas as pd

df = pd.DataFrame(data['barData'], columns=['date', 'open', 'high', 'low' ,'close', 'volume'])

df['date'] = pd.to_datetime(df['date'], unit='s')

print(df)

