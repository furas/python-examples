#!/usr/bin/env python3

#
# API doc: https://portals.aliexpress.com/help.htm?page=help_center_api
#
# Python wrapper: https://github.com/kronas/python-aliexpress-api-client
# (There are some mistakes in example on GitHub)
#

# ---------------------------------------------------------------------
# using external module: aliexpress_api_client
# $ pip install aliexpress_api_client
# or
# $ git clone https://github.com/kronas/python-aliexpress-api-client
# ---------------------------------------------------------------------
# There are some mistakes in example on GitHub
# ---------------------------------------------------------------------

from aliexpress_api_client import AliExpress
from aliexpress_api_client.config import ALIBABA_API_FIELDS

# --- config ---

API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'

aliexpress = AliExpress(API_KEY, AFFILIANTE_ID)

#--- product list ---

print('\n--- product list ---\n')

fields = ['productId', 'productTitle', 'salePrice']
keywords = 'chess'

result = aliexpress.get_product_list(fields, keywords)
#print(result)
products = result['products']

for product in products:
    #print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))
    for name in fields:
        print('%s: %s' % (name, product.get(name, "*** fields doesn't exist ***")))
    print('---')
    
#--- product details ---

print('\n--- product details ---\n')

#fields = ['productId', 'productTitle', 'salePrice']
fields = ALIBABA_API_FIELDS['details']
product_id = 32701355449

product = aliexpress.get_product_details(fields, product_id)

for name in fields:
    #~ if name in product:
        #~ print('%s: %s' % (name, product[name]))
    #~ else:
        #~ print('%s: %s' % (name, "*** fields doesn't exist ***"))

    print('%s: %s' % (name, product.get(name, "*** fields doesn't exist ***")))
print('---')

#--- promotion links ---

#~ fields = ['url', 'promotionUrl']
#~ urls = []

#~ links = api.get_promotion_links(fields, urls)

#~ for link in links['promotionUrls']:
    #~ print '%s: %s' % (link['url'], link['promotionUrl'])

