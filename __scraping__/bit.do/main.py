
# date: 2019.04.21
# https://stackoverflow.com/a/55778640/1832058

import requests

# not need Sessions
s = requests.Session()
s.headers.update({
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
})

#r = s.get('http://bit.do/')
#print(r.status_code)
#print(r.cookies)


# ------------------------------------

headers={
    'X-Requested-With': 'XMLHttpRequest', # need it
    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    #'Cookie': 'permasession=1555801674|ole2ky65f9', #
}

data = {
    'action': 'shorten',
    'url': 'https://onet.pl',
    'url2': ' site2 ', # need spaces
    'url_hash': None,
    'url_stats_is_private': 0,
    'permasession': '1555801674|ole2ky65f9', # need it
}

r = requests.post('http://bit.do/mod_perl/url-shortener.pl', headers=headers, data=data)
print(r.status_code)
print(r.json())



import datetime

datetime.datetime.fromtimestamp(1555801674)


