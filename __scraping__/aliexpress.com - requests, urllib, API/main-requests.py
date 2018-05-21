#!/usr/bin/env python3

#
# API doc: https://portals.aliexpress.com/help.htm?page=help_center_api
#

#----------------------------------------------------------------------
# using external module: requests
# $ pip install requests
#----------------------------------------------------------------------

import requests

API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'

url = 'https://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/' + API_KEY

payload = {
    'fields': ','.join(['productId', 'productTitle', 'salePrice']),
    'keywords': 'chess',
    'highQualityItems': 'yes',
}

response = requests.get(url, params=payload)
#print(response.request.url)
data = response.json()
#print(data)
result = data['result']
#print(result)
products = result['products']

for product in products:
    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))
