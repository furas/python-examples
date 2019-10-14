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
            # current Python keep order in dictionary so it should be always the biggest value at the end of loop
            update_id = item['update_id'] + 1 # to skip older messages
            
            message = item.get('message')
            if message:
                if 'text' in message:
                    print('text:', message['text'])
                if 'photo' in message:
                    print('photo:')
                    pprint(message['photo'])
                if 'voice' in message:
                    print('voice:')
                    pprint(message['voice'])
                # etc.
            else: # it can be ie. `edited_message`
                print('item:')
                pprint(item)

    time.sleep(1)

