
# date: 2019.04.23

import requests
from bs4 import BeautifulSoup
import json

url = 'https://finance.yahoo.com/quote/SPY'
result = requests.get(url)

html = BeautifulSoup(result.content, 'html.parser')
script = html.find_all('script')[-3].text
data = script[112:-12]
print(data[:10], data[-5:])
json_data = json.loads(data)

print(type(json_data))
#print(json_data)
print(json_data.keys())
print(json_data['context'].keys())
print(json_data['context']['dispatcher']['stores']['PageStore']['currentPageName'])
