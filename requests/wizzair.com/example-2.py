#!/usr/bin/env python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    #"Accept-Encoding": "gzip, deflate, sdch, br",
    #"Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
}

s = requests.Session()
print(s.headers)
s.headers.update(headers)

# to get cookies
r = s.get("https://wizzair.com/")

payload = {
    "flightList":[
        {
            "departureStation": "VNO",
            "arrivalStation": "FCO",
            "departureDate": "2017-02-20"
        }
    ],
    "adultCount": 1,
    "childCount": 0,
    "infantCount": 0,
    "wdc": True,
    "dayInterval": 3
}

url = 'https://be.wizzair.com/3.8.2/Api/search/search'

r = s.post(url=url, json=payload)

print(r.text)

data = r.json()

print(data['outboundFlights'][0]['flightNumber'])

for x in data['outboundFlights']:
    print(x['flightNumber'])
