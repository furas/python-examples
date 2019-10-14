#!/usr/bin/env python3

import os
import requests
from pprint import pprint

#token = '<MY TOKEN>'
token = os.environ['TELEGRAM_TOKEN']

# get infromation about bot

url = f'https://api.telegram.org/bot{token}/getMe'
r = requests.get(url)
pprint(r.json())
print('---')

# get messages for bot

url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
pprint(r.json())
print('---')

# ID of first chat - I will use it to send answers
response = r.json()
chat_id = response['result'][0]['message']['chat']['id']
print('chat_id:', chat_id)
print('---')

# send back message 

data = {'chat_id': chat_id, 'text': 'Hello World'}
url = f'https://api.telegram.org/bot{token}/sendMessage'
r = requests.get(url, params=data)

# send back image from internet - I can use POST or GET

data = {'chat_id': chat_id, 'photo': 'https://blog.furas.pl/theme/images/me/furas.png'}
url = f'https://api.telegram.org/bot{token}/sendPhoto'
r = requests.get(url, params=data)
#r = requests.post(url, data=data)
pprint(r.json())
print('---')

# get ID of file on Telegram
response = r.json()
photo_id = response['result']['photo'][0]['file_id']
print('photo_id:', photo_id)
print('---')

# send image which already is on Telegram server - I can use POST or GET

data = {'chat_id': chat_id, 'photo': photo_id}
url = f'https://api.telegram.org/bot{token}/sendPhoto'
r = requests.get(url, params=data)
#r = requests.post(url, data=data)
pprint(r.json())
print('---')

