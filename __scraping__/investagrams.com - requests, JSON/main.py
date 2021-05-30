
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.29
#
# title: Web scraping with bs4 does not return number value
# url: https://stackoverflow.com/questions/67751314/web-scraping-with-bs4-does-not-return-number-value/67751732#67751732

import requests

headers = { 
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.investagrams.com/'
}

params = {
    'stockCode': 'ac',
    'defaultExchangeType': '1',
    'cv': '1622292000-0-',
}

url = 'https://webapi.investagrams.com/InvestaApi/Stock/ViewStock'
r = requests.get(url, params=params, headers=headers)

#print(r.status_code)
#print(r.json())

data = r.json()
print('Open:', data['LatestStockHistory']['Open'])

for key, value in data['LatestStockHistory'].items():
    print(key, '=', value)

