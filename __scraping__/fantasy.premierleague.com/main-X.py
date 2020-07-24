
# author: https://blog.furas.pl
# date: 2020.07.10
# link: https://stackoverflow.com/questions/57403037/how-to-overcome-405-error-on-logging-in-a-site-from-python-requests/

import requests
from bs4 import BeautifulSoup

session = requests.Session()
#session.headers.update({'user-agent': 'Mozilla/5.0'})

login_url = "https://users.premierleague.com/accounts/login/"

# GET page with form
r = session.get(login_url, data=data)
soup = BeautifulSoup(r.content)

data = {
     "login" : "your_login", 
     "password" : "your_password", 
}

# get values from form (except empty places for login and pasword)
for item in soup.find_all('input'):
    key = item['name']
    value = item.get('value')
    if value:
        data[key] = value
    #print(key, '=', value)
    
# POST form data to login
r = session.post(login_url, data=data)

# check if url is different
print(r.url)
print(r.url != login_url)
