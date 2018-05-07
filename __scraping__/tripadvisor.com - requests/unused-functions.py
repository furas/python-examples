#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47858268/1832058
#

import requests               # to get html from server
from bs4 import BeautifulSoup # to search in html

#----------------------------------------------------------------------

# keep request session with all cookies, etc.

session = requests.Session()

session.headers.update({
    # some portals send correct HTML only if you have correct header 'user-agent'
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
})

#----------------------------------------------------------------------

# to get reviews in all languages portal sets cookie 'TALanguage:ALL' 
# but changing cookie manually doesn't work, 
# it gets only english reviews but page gives number of all reviews :(

session.cookies.set('TALanguage', 'ALL', domain='.tripadvisor.com', path='/') # other lanugages ie. 'en', 'es'

url = 'https://www.tripadvisor.com/' # doesn't work
r = session.get(url)

print('TALanguage:', r.cookies.get('TALanguage')) # 'ALL' or 'en' or 'es', etc.
print('TASession:', r.cookies.get('TASession'))   # look for '*LF.ALL*' or '*LF.en*' or '*LF.es*', etc.

#---

session.cookies.set('TALanguage', 'ALL', domain='.tripadvisor.com', path='/') # other lanugages ie. 'en', 'es'

url = 'https://www.tripadvisor.com/Hotel_Review-g294229-d481832-Reviews-Pullman_Jakarta_Indonesia-Jakarta_Java.html'
r = session.get(url)

print('TALanguage:', r.cookies.get('TALanguage')) # 'ALL' or 'en' or 'es', etc.
print('TASession:', r.cookies.get('TASession'))   # look for '*LF.ALL*' or '*LF.en*' or '*LF.es*', etc.

#----------------------------------------------------------------------

# instead cookie 'TALanguage:ALL' better add '?filterLang=ALL' in url and it works.
# it can't be main page 'https://www.tripadvisor.com/',
# it has to be page with place description ie. Hotel Review

#url = 'https://www.tripadvisor.com/?filterLang=ALL' # doesn't work
#url = 'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html?filterLang=ALL'
url = 'https://www.tripadvisor.com/Hotel_Review-g294229-d481832-Reviews-Pullman_Jakarta_Indonesia-Jakarta_Java.html?filterLang=ALL'
r = session.get(url)

print('TALanguage:', r.cookies.get('TALanguage')) # 'ALL' or 'en' or 'es', etc.
print('TASession:', r.cookies.get('TASession'))   # look for '*LF.ALL*' or '*LF.en*' or '*LF.es*', etc.

# Sometimes you can see '?filterLang=ALL' even in cookie 'TAReturnTo' (there are other filters)
print('TAReturnTo:', r.cookies.get('TAReturnTo'))

#----------------------------------------------------------------------

# some session's data you can find in HTML as JavaScript's dictionary

# show all javascripts inside HTML
soup = BeautifulSoup(r.text, 'html.parser')
js = soup.find_all('script')
for idx, x in enumerate(js):
    print('--- js', idx, '---')
    print(x.text[:100])

# read javascript with sessions data and convert to Python's dict
import json
data = json.loads(js[3].text[45:-37])    
print(json.dumps(data, indent=2)) # print JSON with indentions to make it more readable
uid = data['session']['uid']
print('User ID:', uid)

# I try to use UserID in POST request (as browser is doing),
# but it doesn't change cookies 
# so better to add ?filterLang=ALL&...&... in url (GET)

payload = {
    'zff': '',
    'filterSegment': '',
    'zfp': '',
    'amen': '',
    'pRange': '',
    'zfd': '',
    'filterSeasons': '',
    'distFrom': '',
    'zfc': '',
    'q': '',
    'ns': '',
    'trating': '',
    'zfb': '',
    'so': '',
    'filterLang': 'ALL',
    'distFromPnt': '',
    'zft': '',
    'zfn': '',
    't': '',
    'cat': '1',
    'reqNum': '1',
    'changeSet': 'FILTERS,REVIEW_LIST',
    'puid': uid
}

url = 'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html'
session.post(url, data=payload, headers={'x-puid': uid})

print('--- cookies ---')
for x in session.cookies: print(x)
print('--- END ---')
