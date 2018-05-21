#!/usr/bin/env python3

from requests import Session

url = 'https://www.upwork.com/ab/account-security/login'

# Create session to keep all cookies

s = Session()
s.headers.update({
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
})

# GET page to get all cookies

r = s.get(url)

print('\n--- GET: request - headers ---\n')

for key in sorted(r.request.headers):
    print(key, ':', r.request.headers[key])

print('\n--- POST: response - cookies ---\n')
for item in r.cookies:
    print(item)

'''
curl 'https://www.upwork.com/ab/account-security/login'
-H 'Accept: application/json, text/plain, */*' 
--compressed
-H 'Accept-Language: pl,en-US;q=0.7,en;q=0.3'
-H 'Connection: keep-alive'
-H 'Content-Type: application/json;charset=utf-8'
-H 'Cookie: __cfduid=d18c5164f0a05f6a68cd5c4f65e20f08d1525952912; session_id=099654680d41bf837a6dab8295b6a6ce; device_view=full; _vhipo=0; visitor_id=83.23.64.234.1525952912162518; qt_visitor_id=83.23.64.234.1525952912162518; XSRF-TOKEN=396f1b06bf7e8e2b44a35be233855b1b; UserPrivacySettings={%22AlertBoxClosed%22:%222018-05-10T11:49:26.670Z%22%2C%22Groups%22:{%22Targeting%22:true}}'
-H 'DNT: 1'
-H 'Host: www.upwork.com'
-H 'Referer: https://www.upwork.com/ab/account-security/login'
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
-H 'X-Odesk-Csrf-Token: 396f1b06bf7e8e2b44a35be233855b1b'
-H 'X-Odesk-User-Agent: oDesk LM'
-H 'X-Requested-With: XMLHttpRequest'
--data ''
'''

# POST login

payload = {
    'login[username]': 'furas',
    'login[mode]': 'username',
    'login[iovation]': '',
}

headers = {
    'X-Requested-With': 'XMLHttpRequest', # XHR/AJAX
    'X-Odesk-User-Agent': 'oDesk LM',
    'X-Odesk-Csrf-Token': s.cookies['XSRF-TOKEN'],

    'Accept': 'application/json, text/plain, */*', 
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    #'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    #'Cookie': '__cfduid=d18c5164f0a05f6a68cd5c4f65e20f08d1525952912; session_id=099654680d41bf837a6dab8295b6a6ce; device_view=full; _vhipo=0; visitor_id=83.23.64.234.1525952912162518; qt_visitor_id=83.23.64.234.1525952912162518; XSRF-TOKEN=396f1b06bf7e8e2b44a35be233855b1b; UserPrivacySettings={%22AlertBoxClosed%22:%222018-05-10T11:49:26.670Z%22%2C%22Groups%22:{%22Targeting%22:true}}',
    #'DNT': '1',
    'Host': 'www.upwork.com',
    'Referer': 'https://www.upwork.com/ab/account-security/login',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'X-Odesk-Csrf-Token': '396f1b06bf7e8e2b44a35be233855b1b',
    'X-Odesk-User-Agent': 'oDesk LM',
    'X-Requested-With': 'XMLHttpRequest',
}


r = s.post(url, json=payload, headers=headers, data='')

print('\n--- POST: request - headers ---\n')
for key in sorted(r.request.headers):
    print(key, ':', r.request.headers[key])

print('\n---\n')
print('status code:', r.status_code)
print('json:', r.json())

print('\n--- POST: response - headers ---\n')
for key in sorted(r.headers):
    print(key, ':', r.headers[key])

print('\n--- POST: response - cookies ---\n')
for item in r.cookies:
    print(item)


