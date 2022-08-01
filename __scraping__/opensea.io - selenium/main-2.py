# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.30
#

# https://docs.opensea.io/reference/getting-assets

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

#import undetected_chromedriver as uc

# ----

import selenium
print('Selenium:', selenium.__version__)

# ---

url = 'https://opensea.io/collection/meebits?search[sortAscending]=false&search[sortBy]=FAVORITE_COUNT'

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

#driver = uc.Chrome(executable_path='/home/furas/bin/chromedriver', service_args=['--quiet'])
#driver = uc.Chrome()

driver.get(url)

time.sleep(5)

# --- scroll down to the botton ---

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# --- get data ---

assets = []

try:
    item = driver.find_element(By.XPATH, '//h1')
    collection_name = item.text
except NoSuchElementException:
    collection_name = '?'
print('collection_name:', collection_name)

try:
    item = driver.find_element(By.XPATH, '//div[@class="sc-1xf18x6-0 sc-1aqfqq9-0 sc-1y1ib3i-7 haVRLx dfsEJr eGsklH"]')
    collection_desc = item.text
except NoSuchElementException:
    collection_desc = '?'
print('collection_desc:', collection_desc)

for profile in driver.find_elements(By.XPATH, '//div[@role="grid"]/div'):
    print('--- profile ---')

    try:
        item = profile.find_element(By.XPATH, './/div[@class="sc-7qr9y8-0 sc-dw611d-1 iUvoJs fcpvjL"]')
        artname = item.text
    except NoSuchElementException:
        artname = '?'
    print('artname:', artname)

    try:
        item = profile.find_element(By.XPATH, './/div[@class="sc-7qr9y8-0 iUvoJs Price--amount"]')
        price = item.text
    except NoSuchElementException:
        price = '?'
    print('price:', price)

    try:
        item = profile.find_element(By.XPATH, './/a')
        link = item.get_attribute('href')
    except NoSuchElementException:
        link = '?'
    print('link:', link)

    assets.append( [collection_name, artname, price, link] )

print(assets)

import pandas as pd

df = pd.DataFrame(assets, columns=["collection_name", "artname", "price", "link"])
print(df.to_string())

