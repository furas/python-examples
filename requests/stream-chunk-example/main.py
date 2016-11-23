#!/usr/bin/env python3

# example how to use stream

# ---------------------------------------------------------------------
# reading stream in chunks
# ---------------------------------------------------------------------

import requests

url = 'http://httpbin.org/stream/1'

r = requests.get(url, stream=True)


if not r.ok:
    print('Status code:', r.status_code)
else:

    # empty bytes data
    data = b''
    
    for chunk in r.iter_content(32):
        if chunk:  # filter out keep-alive new chunks
            data += chunk
            print(chunk.decode('utf-8'), '\n----')

    # convert bytes to string and print
    print(data.decode('utf-8'))

# ---------------------------------------------------------------------
# writing to file 
# ---------------------------------------------------------------------

import requests

url = 'http://httpbin.org/stream/1'

r = requests.get(url, stream=True)

if not r.ok:
    print('Status code:', r.status_code)
else:

    with open('output.txt', 'wb') as f:
        for chunk in r.iter_content(32):
            # not sure if `chunk` can be empty
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # flush python buffer and OS buffrer
                #f.flush()
                #os.fsync(f.fileno())

# ---------------------------------------------------------------------
# using Response.raw and shutil.copyfileobj()
# ---------------------------------------------------------------------
# http://docs.python-requests.org/en/master/api/#requests.Response.raw
# https://docs.python.org/3/library/shutil.html#shutil.copyfileobj
# ---------------------------------------------------------------------

import requests
import shutil

url = 'http://httpbin.org/stream/1'

r = requests.get(url, stream=True)

if not r.ok:
    print('Status code:', r.status_code)
else:

    with open'output.txt', 'wb') as f:
        shutil.copyfileobj(r.raw, f)

