#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47875952/1832058
#

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
    
'''
Result:

OK: ok
Symbol: ADBL
Name: Agriculture Development Bank Limited
  date: 12/18/2016
  open: 540.0
 close: 540.0
  high: 540.0
   low: 525.0
volume: 6847.0
   rsi: 0.0
----------------------
  date: 12/19/2016
  open: 535.0
 close: 520.0
  high: 535.0
   low: 520.0
volume: 6963.0
   rsi: 0.0
----------------------
  date: 12/20/2016
  open: 520.0
 close: 520.0
  high: 530.0
   low: 505.0
volume: 9974.0
   rsi: 0.0
----------------------
'''    
    
