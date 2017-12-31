from selenium import webdriver
import time

#
# https://stackoverflow.com/a/48042058/1832058
# 

# --- Selenium ---

url = 'https://koinex.in/'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(8)

#tables = driver.find_elements_by_tag_name('table')
#for item in tables:
#    print(item.text)

# --- convert cookies/headers from Selenium to Requests ---

cookies = driver.get_cookies()

for item in cookies:
    print('name:', item['name'])
    print('value:', item['value'])
    print('path:', item['path'])
    print('domain:', item['domain'])
    print('expiry:', item['expiry'])
    print('secure:', item['secure'])
    print('httpOnly:', item['httpOnly'])
    print('----')

# convert list of dictionaries into dictionary
cookies = {c['name']: c['value'] for c in cookies}

# it has to be full `User-Agent` used in Browser/Selenium (it can't be short 'Mozilla/5.0')
headers = {'User-Agent': driver.execute_script('return navigator.userAgent')}

# --- requests + BeautifulSoup ---

import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update(headers)
s.cookies.update(cookies)

r = s.get(url)

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
tables = soup.find_all('table')

print('tables:', len(tables))

for item in tables:
    print(item.get_text())
