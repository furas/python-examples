
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.21
# https://docs.aiohttp.org/en/stable/index.html
# https://stackoverflow.com/questions/65371754/aiohttp-web-post-method-get-params/

# --- POST data ---

import requests

r = requests.post('http://0.0.0.0:8080/test', data={'param1': 'value1', 'param2': 'value2'})
print(r.text)

