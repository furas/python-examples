import requests
from lxml import html
import json

# date: 2017.12.22
# https://stackoverflow.com/a/47935432/1832058

url = "http://www.amazon.com/dp/B008HDREZ6"

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
}

response = requests.get(url, headers=headers)
doc = html.fromstring(response.content)

print('--- small ---')
XPATH_IMAGE = '//div[@id="altImages"]//img/@src'
RAW_IMAGE = doc.xpath(XPATH_IMAGE)
print('\n'.join(RAW_IMAGE[:-1]))

print('--- scripts ---')
XPATH_SCRIPTS = '//script'
RAW_SCRIPTS = doc.xpath(XPATH_SCRIPTS)
data = ''
for script in RAW_SCRIPTS:
    text = script.text 
    if 'data["colorImages"]' in text:
        for line in text.splitlines():
            if 'data["colorImages"]' in line:
                #print(line)
                data = line

print('--- data ---')
data = data[24:-1]
data = json.loads(data)

print('keys:', data.keys())
print('keys:', data['Silver'][0].keys())
print('keys:', data['White'][0].keys())

for item in data['Silver']:
    print('variant:', item['variant'])
    print('main:', item['main'])
    print('large:', item['large'])
    print('hiRes:', item['hiRes'])
    print('thumb:', item['thumb'])
    print('-----')
    
