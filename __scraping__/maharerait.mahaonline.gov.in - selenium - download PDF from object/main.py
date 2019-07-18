
# date: 2019.07.18
# https://stackoverflow.com/questions/57088227/save-the-pdf-using-the-selenium-webdriver-in-python/57089444#57089444

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
from bs4 import BeautifulSoup
import os
from selenium.webdriver.support.select import Select
import time

url = 'https://maharerait.mahaonline.gov.in'
#chrome_path = r'C:/Users/User/AppData/Local/Programs/Python/Python36/Scripts/chromedriver.exe'

driver = webdriver.Firefox()#executable_path=chrome_path)
driver.get(url)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='search-pro-details']//a[contains(.,'Search Project Details')]"))).click()
Registered_Project_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"Promoter")))

driver.execute_script("arguments[0].click();",Registered_Project_radio)

Application = driver.find_element_by_id("CertiNo")
Application.send_keys("P50500000005")

Search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"btnSearch")))
driver.execute_script("arguments[0].click();", Search)
View = [item.get_attribute('href') for item in driver.find_elements_by_tag_name("a") if item.get_attribute('href') is not None]

btn = WebDriverWait(driver, 
     20).until(EC.element_to_be_clickable((By.XPATH, 
     "//a[@class='btn btn-md btn-success' and @id='btnShow_2017']")))

driver.execute_script("arguments[0].click();",btn)

time.sleep(5)

obj = driver.find_element_by_tag_name('object')
data = obj.get_attribute('data')
text = data.split(',')[1]

import base64
bytes = base64.b64decode(text)

with open('output.pdf', 'wb') as fp:
    fp.write(bytes)
