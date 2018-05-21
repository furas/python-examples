Folder `aliexpress_api_client` from [https://github.com/kronas/python-aliexpress-api-client](https://github.com/kronas/python-aliexpress-api-client)

API doc: [https://portals.aliexpress.com/help.htm?page=help_center_api](https://portals.aliexpress.com/help.htm?page=help_center_api)



urllib 
============


requests
============



AliExpress API Client
============


Python client library for AliExpress API

Usage example
------------

**Configuration:**
``` python
from aliexpress_api_client import AliExpress

aliexpress = AliExpress('api_key', 'affiliate_id')
```

**Get product list:**

There was mistake in example on [https://github.com/kronas/python-aliexpress-api-client](https://github.com/kronas/python-aliexpress-api-client). 

`get_product_list()` expects second argument `keywords`. And it doesn't return directly `products` - they are in `result['products']`

``` python

fields = ['productId', 'productTitle', 'salePrice']
keywords = 'chess'

result = aliexpress.get_product_list(fields, keywords)
products = result['products']

for product in products:
    print '#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice'])
```

**Get product details:**
``` python
product = aliexpress.get_product_details(['productId', 'productTitle', 'salePrice'], product_id)

print '#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice'])
```

**Get promotion links (require `affiliate_id`):**
```
links = api.get_promotion_links(['url', 'promotionUrl'], urls)

for link in links['promotionUrls']:
    print '%s: %s' % (link['url'], link['promotionUrl'])
```

---

## URL (in `aliexpress_api_client.config`)

ALIBABA_API_URL = 'http://gw.api.alibaba.com/openapi/param2/2/portals.open/%(api_call)s/%(api_key)s?%(call_parameters)s'

## Methods in class AliExpress

- get_product_list(self, fields, keywords, **kwargs):
- get_product_details(self, fields, product_id):
- get_promotion_links(self, fields, urls, tracking_id=None):

## Constants/Dictionares in `aliexpress_api_client.config`

- ALIBABA_API_CALLS
- ALIBABA_API_PARAMS
- ALIBABA_API_FIELDS
- ALIBABA_API_CATEGORIES
- ALIBABA_API_ERROR_CODES

---

Oryginal API has more methods

    listPromotionProduct        promotion products
    getPromotionProductDetail   promotion product detail
    getPromotionLinks           generate ad links for promotion products
    listPromotionCreative       list promotion banner
    getCompletedOrders          get order detail when it's status is pay or completed
    getOrderStatus              get order detail when it's status is pay or completed by orderIds
    listHotProducts             hot products at aliexpress
    listSimilarProducts         recommened similar products at aliexpress
    getItemByOrderNumbers       get product info by order numbers
    getAppPromotionProduct      get product info at apps

API doc: [https://portals.aliexpress.com/help.htm?page=help_center_api](https://portals.aliexpress.com/help.htm?page=help_center_api)
