
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.21
# https://docs.aiohttp.org/en/stable/index.html
# https://stackoverflow.com/questions/65371754/aiohttp-web-post-method-get-params/

# --- FILES data ---

import requests

r = requests.post('http://0.0.0.0:8080/test', files=[('file', open('client.py'))])
print(r.text)

