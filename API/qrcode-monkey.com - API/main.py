# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.25

import requests
import json

URL = "https://api.qrcode-monkey.com/qr/custom"

def get():
    # it needs to convert `config` to `json` manually
    
    payload = {
        "data": "https://blog.furas.pl",
        "config": json.dumps({
            "body": "circle"
        }),
        "size": 300,
        "download": False,
        "file": "png"
    }
        
    return requests.get(URL, params=payload)

def post():
    # it converts `config` to `json` automatically (because it sends all `payload` as `json`)

    payload = {
        "data": "https://blog.furas.pl",
        "config": {
            "body": "circle",
        },
        "size": 300,
        "download": False,
        "file": "png"
        }
        
    return requests.post(URL, json=payload)

# --- main ---

print('\n--- GET ---\n')

response = get()

print('status:', response.status_code)
print('url:', response.url)
print(response.text[:100])

with open('QR_GET.png', 'wb') as f:
    f.write(response.content)
    
print('\n--- POST ---\n')

response = post()

print('status:', response.status_code)
print('url:', response.url)
print(response.text[:100])

with open('QR_POST.png', 'wb') as f:
    f.write(response.content)

print('---')
