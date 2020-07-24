#!/usr/bin/env python3

# author: https://blog.furas.pl
# date: 2020.07.11
# 
from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get("https://finance.yahoo.com/quote/INFY/news?p=INFY")

for i in range(20):
       driver.execute_script("window.scrollBy(0, 250)")
       time.sleep(1)

all_items = driver.find_elements_by_xpath('//*[@id="latestQuoteNewsStream-0-Stream"]/ul/li')

#for item in all_items:
#    print(item.find_element_by_xpath('.//h3/a').text)
#    print(item.find_element_by_xpath('.//p').text)
#    print('---')
    
print(all_items[-1].find_element_by_xpath('.//h3/a').text)
print(all_items[-1].find_element_by_xpath('.//p').text)

