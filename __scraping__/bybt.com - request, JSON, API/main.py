
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.18
#
# title: API call function variable not set properly
# url: https://stackoverflow.com/questions/68040342/api-call-function-variable-not-set-properly/

# Doc: https://bybt.gitbook.io/bybt/api-key  

# mistake in documentation: it has to be `params=...` instead of `data=...`

# Doc: https://bybt.gitbook.io/bybt/futures/exchange-open-interest


# The same in curl needs parameters directly in URL
# curl -H 'bybtSecret: API_KEY' 'https://open-api.bybt.com/api/pro/v1/futures/openInterest?interval=2&symbol=ETH'

import requests

url = 'https://open-api.bybt.com/api/pro/v1/futures/openInterest'

payload = {
    'interval': 2,    # it can be interger 2 or string "2"
    'symbol': 'ETH',
}

headers = {
    'bybtSecret': 'API_KEY'  # 'ced..........................2A4'  # 32 chars
}

response = requests.get(url, headers=headers, params=payload)

print('URL:', response.url)

print('Text:', response.text)

data = response.json()

print(   'Code:', data['code'])
print('Success:', data['success'])
print('Message:', data['msg'])

if data['success']:
    for item in data['data']:
        print('item:', item['symbol'], item['openInterest'])
        
