
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.21
# https://docs.aiohttp.org/en/stable/index.html
# https://stackoverflow.com/questions/65371754/aiohttp-web-post-method-get-params/

# --- JSON ---

import requests

r = requests.post('http://0.0.0.0:8080/test', json={'param1': 'value1', 'param2': 'value2'})
print(r.text)

# --- JSON ---

import requests
import json

r = requests.post('http://0.0.0.0:8080/test', 
                  data=json.dumps({'param1': 'value1', 'param2': 'value2'}),
                  headers={'Content-Type': 'application/json'},
                 )
print(r.text)

# --- POST data ---

import requests

r = requests.post('http://0.0.0.0:8080/test', data={'param1': 'value1', 'param2': 'value2'})
print(r.text)

# --- URL data ---

import requests

r = requests.post('http://0.0.0.0:8080/test', params={'param1': 'value1', 'param2': 'value2'})
print(r.text)

# --- FILES data ---

import requests

r = requests.post('http://0.0.0.0:8080/test', files=[('file', open('client.py'))])
print(r.text)

