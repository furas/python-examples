#!/usr/bin/env python3

# date: 2020.05.18
# https://stackoverflow.com/questions/61858764/is-there-an-easy-way-to-access-all-transactions-recorded-in-a-bitcoin-block-with/
# 
# https://www.blockchain.com/api/blockchain_api

import requests

r = requests.get('https://blockchain.info/block-height/100?format=json')
data = r.json()

#print(r.text)
#print(data)
print(data['blocks'][0]['hash'])
