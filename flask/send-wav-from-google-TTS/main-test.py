#!/usr/bin/env python3 

# date: 2019.12.11
# 

import requests
import os

data = 'Hello World'

r = requests.post('http://127.0.0.1:5000/', json=data)

open('output.wav', 'wb').write(r.content)

os.system('mplayer output.wav')
