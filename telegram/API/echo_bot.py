#!/usr/bin/env python3

import os
import requests
import time
from pprint import pprint

#token = '<MY TOKEN>'
token = os.environ['TELEGRAM_TOKEN']

print('Running ...')

# to skip older messages
update_id = 0

while True:
    # get messages
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url, params={'offset': update_id}) # `offset` to skip older messages
    data = r.json()

    if not data['ok']:
        print('ERROR:', data)
    else:
        for item in data['result']:
            update_id = item['update_id'] + 1 # to skip older messages
            
            message = item.get('message')
            if message:
                if 'text' in message:
                    chat_id = message['chat']['id']
                    url = f'https://api.telegram.org/bot{token}/sendMessage'
                    r = requests.get(url, params={'chat_id': chat_id, 'text': message['text']})
                    print('response:', r.json())                    
                if 'photo' in message:
                    chat_id = message['chat']['id']
                    url = f'https://api.telegram.org/bot{token}/sendPhoto'
                    r = requests.get(url, params={'chat_id': chat_id, 'photo': message['photo'][0]['file_id']})
                    print('response:', r.json())                    
                if 'voice' in message:
                    print('voice:')
                    pprint(message['voice'])
                # etc.
            else: # it can be ie. `edited_message`
                print('item:')
                pprint(item)

    time.sleep(1)

