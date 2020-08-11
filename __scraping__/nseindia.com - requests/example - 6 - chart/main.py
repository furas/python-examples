
# author: Bartłomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.08.12
# link: (stackoverflow) https://stackoverflow.com/questions/63362688/how-can-i-grab-data-from-a-nse-chart-with-python/

# https://www.nseindia.com/get-quotes/equity?symbol=BERGEPAINT

import requests
import datetime

headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://www.nseindia.com/api/chart-databyindex?index=BERGEPAINTEQN'
#url = 'https://www.nseindia.com/api/chart-databyindex?index=BERGEPAINTEQN&preopen=true'

r = requests.get(url, headers=headers)

# --- response ---

#print(r.status_code)

data = r.json()

print('name:', data['name'])
print('identifier:', data['identifier'])
print('close price:', data['closePrice'])

prices = data['grapthData'][:10]

for item in prices:
    dt = datetime.datetime.utcfromtimestamp(item[0]/1000)
    value = item[1]
    print(dt, value)
    
