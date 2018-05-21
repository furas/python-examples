ALIBABA_API_URL = 'http://gw.api.alibaba.com/openapi/param2/2/portals.open/%(api_call)s/%(api_key)s?%(call_parameters)s'

ALIBABA_API_CALLS = {
    'list': 'api.listPromotionProduct',
    'details': 'api.getPromotionProductDetail',
    'links': 'api.getPromotionLinks'
}

ALIBABA_API_PARAMS = {
    'list': [
        'fields',
        'keywords',
        'categoryId',
        'originalPriceFrom',
        'originalPriceTo',
        'volumeFrom',
        'volumeTo',
        'pageNo',
        'pageSize',
        'sort',
        'startCreditScore',
        'endCreditScore',
        'highQualityItems',
        'localCurrency',
        'language'
    ],
    'details': [
        'fields',
        'productId'
    ],
    'links': [
        'fields',
        'trackingId',
        'urls'
    ]
}

ALIBABA_API_FIELDS = {
    'list': [
        'totalResults',
        'productId',
        'productTitle',
        'productUrl',
        'imageUrl',
        'originalPrice',
        'salePrice',
        'discount',
        'evaluateScore',
        'commission',
        'commissionRate',
        '30daysCommission',
        'volume',
        'packageType',
        'lotNum',
        'validTime',
        'localPrice',
        'allImageUrls'
    ],
    'details': [
        'productId',
        'productTitle',
        'productUrl',
        'imageUrl',
        'originalPrice',
        'salePrice',
        'discount',
        'evaluateScore',
        'commission',
        'commissionRate',
        '30daysCommission',
        'volume',
        'packageType',
        'lotNum',
        'validTime',
        'storeName',
        'storeUrl',
        'allImageUrls',
    ],
    'links': [
        'totalResults',
        'trackingId',
        'publisherId',
        'url',
        'promotionUrl',
        'localPrice'
        
    ]
}

ALIBABA_API_CATEGORIES = {
    3: 'Apparel & Accessories',
    34: 'Automobiles & Motorcycles',
    1501: 'Baby Products',
    66: 'Beauty & Health',
    7: 'Computer & Networking',
    13: 'Construction & Real Estate',
    44: 'Consumer Electronics',
    100008578: 'Customized Products',
    5: 'Electrical Equipment & Supplies',
    502: 'Electronic Components & Supplies',
    2: 'Food',
    1503: 'Furniture',
    200003655: 'Hair & Accessories',
    42: 'Hardware',
    15: 'Home & Garden',
    6: 'Home Appliances',
    200003590: 'Industry & Business',
    36: 'Jewelry & Watch',
    39: 'Lights & Lighting',
    1524: 'Luggage & Bags',
    21: 'Office & School Supplies',
    509: 'Phones & Telecommunications',
    30: 'Security & Protection',
    322: 'Shoes',
    200001075: 'Special Category',
    18: 'Sports & Entertainment',
    1420: 'Tools',
    26: 'Toys & Hobbies',
    1511: 'Watches',
    320: 'Wedding & Events'
}

ALIBABA_API_ERROR_CODES = {
    'list': {
        20010000: 'Call succeeds',
        20020000: 'System Error',
        20030000: 'Unauthorized transfer request',
        20030010: 'Required parameters',
        20030020: 'Invalid protocol format',
        20030030: 'API version input parameter error',
        20030040: 'API name space input parameter error',
        20030050: 'API name input parameter error',
        20030060: 'Fields input parameter error',
        20030070: 'Keyword input parameter error',
        20030080: 'Category ID input parameter error',
        20030090: 'Tracking ID input parameter error',
        20030100: 'Commission rate input parameter error',
        20030110: 'Original Price input parameter error',
        20030120: 'Discount input parameter error',
        20030130: 'Volume input parameter error',
        20030140: 'Page number input parameter error',
        20030150: 'Page size input parameter error',
        20030160: 'Sort input parameter error',
        20030170: 'Credit Score input parameter error'
    },
    'details': {
        20010000: 'Call succeeds',
        20020000: 'System Error',
        20030000: 'Unauthorized transfer request',
        20030010: 'Required parameters',
        20030020: 'Invalid protocol format',
        20030030: 'API version input parameter error',
        20030040: 'API name space input parameter error',
        20030050: 'API name input parameter error',
        20030060: 'Fields input parameter error',
        20030070: 'Product ID input parameter error'
    },
    'links': {
        20010000: 'Call succeeds',
        20020000: 'System Error',
        20030000: 'Unauthorized transfer request',
        20030010: 'Required parameters',
        20030020: 'Invalid protocol format',
        20030030: 'API version input parameter error',
        20030040: 'API name space input parameter error',
        20030050: 'API name input parameter error',
        20030060: 'Fields input parameter error',
        20030070: 'Tracking ID input parameter error',
        20030080: 'URL input parameter error or beyond the maximum number of the URLs'
    }
}
