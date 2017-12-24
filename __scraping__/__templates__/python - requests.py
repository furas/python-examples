#!/usr/bin/env python3

import requests

url = 'http://httpbin.org/post'

headers = {
    #'User-Agent': '',
    'Content-type': 'application/octet-stream',
}

payload = {
    'A': 123,
    'B': 'abc',
    'C': None,
}

binary_data = b'hello world'

proxy = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080',
}

r = requests.post(url, headers=headers, proxies=proxy,
                    params=payload, data=binary_data)

print('--- requests ---')
print(r.url)
print(r.request.headers)
print(r.request.body)

print('--- response ---')
print(r.headers)
print(r.content)
print(r.text)
print(r.json())
