
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.10.06
#
# title: Can't get size of elements and the classes in selenium
# url: https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487

# [Can't get size of elements and the classes in selenium](https://stackoverflow.com/questions/69458094/cant-get-size-of-elements-and-the-classes-in-selenium/69459487#69459487)

# [API - Tokens](https://docs.etherscan.io/api-endpoints/tokens)
# [API - Contracts](https://docs.etherscan.io/api-endpoints/contracts)

#import os
import requests

#API_KEY = os.getenv(TOKEN_ETHERSCAN)
API_KEY = '7Cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

url = 'https://api.etherscan.io/api'

payload = {
   'module': 'stats',
   'action': 'tokeninfo',
   'contractaddress': 0xB8c77482e45F1F44dE1745F52C74426C631bDD52,
   'apikey': API_KEY,
}

r = requests.get(url, params=payload)   
print(r.text)

