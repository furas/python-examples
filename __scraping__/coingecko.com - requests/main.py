
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.07
#
# title: Im trying login a website with requests in python
# url: https://stackoverflow.com/questions/69871652/im-trying-login-a-website-with-requests-in-python/69872661#69872661

# [Im trying login a website with requests in python](https://stackoverflow.com/questions/69871652/im-trying-login-a-website-with-requests-in-python/69872661#69872661)

# https://github.com/man-c/pycoingecko

import requests
import json
import urllib

s = requests.Session()

# ---

url = "https://www.coingecko.com/accounts/csrf_meta.json"

r = s.get(url)

token = r.json()["token"]

# ---

data = {
    "utf8": "✓",
    "authenticity_token": token,
    "user[email]": "me@domain.com",
    "user[password]": "my_password",
    "user[redirect_to]": "https://www.coingecko.com/en",
    "user[remember_me]": ["0"]
}

url = "https://www.coingecko.com/account/sign_in?locale=en"

r = s.post(url, data=data)
#print(r.text)

cookies = s.cookies.get_dict() 
print('cookies:', cookies)

if 'flash' in cookies:
    flash = cookies['flash']
    flash = urllib.parse.unquote_plus(flash)
    flash = json.loads(flash)
    print('flask:', flash[0][1])

