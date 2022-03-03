# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.27
# [web scraping - Response 403 Error When Trying to Login To Website Using Python Requests - Stack Overflow](https://stackoverflow.com/questions/71288666/response-403-error-when-trying-to-login-to-website-using-python-requests/71288885#71288885)

import requests

session = requests.session()

# --- GET ---

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
          }

url_get = 'https://app.mapro.us/en/login'

p = session.get(url_get, headers=headers)

print(p)
#print(p.text)
print('Cookies SID:', session.cookies.get('SID'))

# --- POST ---

username = 'username'
password = 'password'

login_info = {'login': username, 'pwd': password}

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'application/json, text/javascript, */*; q=0.01',  # expect JSON 
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',  # send AJAX
          }

url_post = 'https://app.mapro.us/ajax?login='

p = session.post(url_post, headers=headers, data=login_info)

print(p)
print(p.text)


