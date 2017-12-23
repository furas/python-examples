#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47859609/1832058
#

import requests
import bs4

site_url = "https://www.cv-library.co.uk/companies/agencies/0-9"
phone_url = "https://www.cv-library.co.uk/account-contact-details?id="

session = requests.Session()
session.headers.update({
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
#    "Accept-Encoding": "gzip, deflate", 
    #"Accept-Language": "pl,en-US;q=0.7,en;q=0.3", 
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
})
print(session.headers)

r = session.get(site_url)
print(r.status_code)
soup = bs4.BeautifulSoup(r.text, 'html.parser')

#print(r.text)
all_p = soup.find_all('p', class_='company-profile-phone')

for p in all_p:
    number = p.a['onclick'][22:-2]
    print('Phone ID:', number)

    session.headers.update({
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    })

    r = session.get(phone_url + number)

    if r.status_code != 200:
        print("Contact details view limit reached")
    else:
        data = r.json()

        if "email" in data:
            print('email:', data['email'])
        if "phone" in data:
            print('phone:', data['telephone'])
    print('---')
