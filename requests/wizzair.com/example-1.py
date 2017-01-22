#!/usr/bin/env python3

import requests

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

r = s.post(url, json=payload)

print(r.text)

data = r.json()

print(data['outboundFlights'][0]['flightNumber'])

for x in data['outboundFlights']:
    print(x['flightNumber'])
