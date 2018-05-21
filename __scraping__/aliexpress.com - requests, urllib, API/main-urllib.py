#!/usr/bin/env python3

#
# API doc: https://portals.aliexpress.com/help.htm?page=help_center_api
#

#----------------------------------------------------------------------
# using standard modules: urllib, json
#----------------------------------------------------------------------

import urllib.request, urllib.parse
import json

API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'

API_KEY = '9420'
AFFILIANTE_ID = 'bazaarmaya'

url = 'https://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/' + API_KEY

payload = {
    'fields': ','.join(['productId', 'productTitle', 'salePrice']),
    'keywords': 'chess',
    'highQualityItems': 'yes',
}

response = urllib.request.urlopen(url + '?' + urllib.parse.urlencode(payload))
data = json.loads(response.read())
#print(data)
result = data['result']
#print(result)
products = result['products']

for product in products:
    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))

