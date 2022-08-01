# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.29
# 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

import time

# ----

import selenium
print('Selenium:', selenium.__version__)

# ---

website = 'https://opensea.io/collection/azuki?search[sortAscending]=false&search[sortBy]=FAVORITE_COUNT'

#s = Service('C:\webdrivers\chromedriver.exe')
#driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get(website)
driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, '//div[@class="sc-1xf18x6-0 sc-1aqfqq9-0 haVRLx dfsEJr styledPhoenixText"]').click()

collection_name  = []
collection_desc1 = []
collection_desc2 = []
collection_desc3 = []
name  = []
price = []

for item in driver.find_elements(By.XPATH, '//h1'):
    collection_name.append(item.text)
    #time.sleep(1)

for item in driver.find_elements(By.XPATH, '(//p[1])[1]'):
    collection_desc1.append(item.text)
    #time.sleep(1)

for item in driver.find_elements(By.XPATH, '//p[2]'):
    collection_desc2.append(item.text)
    #time.sleep(1)
    
for item in driver.find_elements(By.XPATH, '//p[3]'):
    collection_desc3.append(item.text)
    #time.sleep(1)

for item in driver.find_elements(By.XPATH, '//div[@class="sc-7qr9y8-0 sc-dw611d-1 iUvoJs fcpvjL"]'):
    name.append(item.text)
    #time.sleep(1)

for item in driver.find_elements(By.XPATH, '//div[@class="sc-7qr9y8-0 iUvoJs Price--amount"]'):
    price.append(item.text)
    #time.sleep(1)

Collection_Azuki = {
    'Collection_Name': collection_name,
    'Collection_Description1': collection_desc1,
    'Collection_Des2': collection_desc2,
    'Colltionec_Des3': collection_desc3,
    'Art_Name_fav': name,
    'Art_Price_fav': price
}

import pandas as pd

df = pd.DataFrame.from_dict(Collection_Azuki, orient='index')
df = df.transpose()

print(df.to_string())
