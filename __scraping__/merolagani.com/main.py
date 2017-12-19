#!/usr/bin/env python3

import requests

url = 'http://merolagani.com/handlers/webrequesthandler.ashx?type=get_company_graph&symbol=ADBL&dateRange=1'
#       http://merolagani.com/handlers/webrequesthandler.ashx?type=get_company_graph&symbol=ADBL&dateRange=12
r = requests.get(url)

data = r.json()

print('Status:', data['msgType'])
print('Symbol:', data['symbol'])
print('Name:', data['name'])
print('Number:', len(data['quotes']))

for row in data['quotes']:
    print('  date:', row['date'])
    print('  open:', row['open'])
    print(' close:', row['close'])
    print('  high:', row['high'])
    print('   low:', row['low'])
    print('volume:', row['volume'])
    print('   rsi:', row['rsi'])
    print('----------------------')
