#!/usr/bin/env python3 

# date: 2019.12.18
# ???

import requests 

url = "https://httpbin.org/ip"

proxy = {
    #"http": '141.125.82.106:80'
    "https": '141.125.82.106:80'
}

r = requests.get(url, timeout=200, proxies=proxy)

print(r.text)
