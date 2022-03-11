
import requests

url = "https://api.nvidia.partners/edge/product/search"

params = {
    'page': '1',
    'limit': '9',
    'locale': 'fr-fr',
    'category': 'GPU',
    'gpu': 'RTX 3090,RTX 3080 Ti,RTX 3080,RTX 3070 Ti,RTX 3070,RTX 3060 Ti,RTX 3060,RTX 3050 Ti',
    'manufacturer': 'NVIDIA', 
    'gpu_filter': 'RTX 3090~1,RTX 3080 Ti~1,RTX 3080~1,RTX 3070 Ti~1,RTX 3070~1,RTX 3060 Ti~1,RTX 3060~0,RTX 3050 Ti~0,RTX 3050~0,RTX 2080 SUPER~0,RTX 2080~0,RTX 2070 SUPER~0,RTX 2070~0,RTX 2060 SUPER~0,RTX 2060~0,GTX 1660 Ti~0,GTX 1660 SUPER~0,GTX 1660~0,GTX 1650 Ti~0,GTX 1650 SUPER~0,GTX 1650~0'
}

# it needs User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for details in data["searchedProducts"]["productDetails"]:

    if details['prdStatus'] == "out_of_stock":
    
        print("{:<10} | {:30} | {}".format(details["productSKU"], details["productTitle"], details["productPrice"]))
        
        #for item in details['retailers']:
        #    print('link:', item['purchaseLink'])
        
        # OR
        
        print('link:', details['retailers'][0]['purchaseLink'])
