#!/usr/bin/env python3 

# date: 2019.12.18
# ???

import requests 
from bs4 import BeautifulSoup

def main(request):
    soup = BeautifulSoup(request.content, "html.parser")
    return soup.find('font').b.contents[0]
    
url = "https://www.ipchicken.com/"

proxies = {
   #"http": '141.125.82.106:80',
   "https": '141.125.82.106:80',
}

r = requests.get(url, proxies=proxies)

ip = main(r)

print(ip)
