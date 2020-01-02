#!/usr/bin/env python3 

# date: 2020.01.02
# ???

import requests

url = 'https://api.pcloud.com/uploadfile'

files = {
    'file': open('folder/image.jpg', 'rb')
}

data = {
    'username': 'user@example.com',
    'password': 'top-secret-word',
}

r = requests.post(url, data=data, files=files)

print(r.text)
