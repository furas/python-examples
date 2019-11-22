#!/usr/bin/env python3

# date: 2019.10.29
# 

import requests
import polling

# --- 

result = polling.poll(lambda: requests.get('http://google.com').status_code == 200, step=60, poll_forever=True)
print(result)

# True

# ---

def check(response):
    return response.status_code == 200

result = polling.poll(lambda: requests.get('http://google.com'), step=60, poll_forever=True, check_success=check)
print(result.text)

# HTML

