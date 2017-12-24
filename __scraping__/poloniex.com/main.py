#!/usr/bin/env python3

import requests

url = 'https://poloniex.com/public'

params = {
    'command': 'returnTradeHistory',
    'currencyPair': 'BTC_NXT',
    'start': '1410158341',
    'end': '1410499372',
}

response = requests.get(url, params=params)

print('url:', response.request.url)
print('-----')

data = response.json()

print('data lenght:', len(data))
print('-----')

print('data[0].keys;', data[0].keys())
print('-----')

for item in data[:3]:
    print('globalTradeID:', item['globalTradeID'])
    print('      tradeID:', item['tradeID'])
    print('         date:', item['date'])
    print('         type:', item['type'])
    print('         rate:', item['rate'])    
    print('       amount:', item['amount'])    
    print('        total:', item['total'])
    print('-----')
