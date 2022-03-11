# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.07
# [Can get data in json in Python - Stack Overflow](https://stackoverflow.com/questions/71351318/can-get-data-in-json-in-python/71355804#71355804)

import requests

url = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=fr-fr&category=GPU&gpu=RTX%203090,RTX%203080%20Ti,RTX%203080,RTX%203070%20Ti,RTX%203070,RTX%203060%20Ti,RTX%203060,RTX%203050%20Ti&manufacturer=NVIDIA&gpu_filter=RTX%203090~1,RTX%203080%20Ti~1,RTX%203080~1,RTX%203070%20Ti~1,RTX%203070~1,RTX%203060%20Ti~1,RTX%203060~0,RTX%203050%20Ti~0,RTX%203050~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20Ti~0,GTX%201650%20SUPER~0,GTX%201650~0"

# it needs User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

response = requests.get(url, headers=headers)
data = response.json()

for details in data["searchedProducts"]["productDetails"]:

    if details['prdStatus'] == "out_of_stock":
    
        print("{:<10} | {:30} | {}".format(details["productSKU"], details["productTitle"], details["productPrice"]))
        
        #for item in details['retailers']:
        #    print('link:', item['purchaseLink'])
        
        # OR
        
        print('link:', details['retailers'][0]['purchaseLink'])
