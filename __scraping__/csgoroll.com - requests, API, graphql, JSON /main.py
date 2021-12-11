
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.28
#
# title: Can I extract JSON data from this XHR request?
# url: https://stackoverflow.com/questions/70139968/can-i-extract-json-data-from-this-xhr-request/70141474#70141474

# [Can I extract JSON data from this XHR request?](https://stackoverflow.com/questions/70139968/can-i-extract-json-data-from-this-xhr-request/70141474#70141474)

import requests

url = 'https://api.csgoroll.com/graphql'

headers = {
    'User-Agent': 'Mozilla/5.0',
#    'Accept': 'application/json, text/plain, */*',
}

params = {
    'operationName': 'TradeList',
    'variables': '{"first":50,"orderBy":"TOTAL_VALUE_DESC","status":"LISTED","steamAppName":"CSGO"}',
    'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"87239fc5fa143cf0437964a20937aa558145cc8385eae48ca8734cb16abfd266"}}',
}

r = requests.get(url, headers=headers, params=params)
#print(r.text)

data = r.json()
trades = data['data']['trades']['edges']

for trade in trades:
    #print(item)
    for item in trade['node']['tradeItems']:
        print(item['marketName'])
