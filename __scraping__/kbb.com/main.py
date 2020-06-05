#!/usr/bin/env python3

# date: 2020.06.05
# https://stackoverflow.com/questions/62211750/how-to-extract-text-from-svg-using-python-selenium/

# it needs IP in location US to display page
# I used free VPN https://windscribe.com/?affid=kez9ypcg with program installed on Linux Mint

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.kbb.com/cadillac/deville/1996/sedan-4d/'

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)

# doesn't work - always empty list
#price_xpaths = driver.find_elements_by_xpath(".//*[name()='svg']//*[name()='g']//*[name()='text']")
#price_xpaths = driver.find_elements_by_xpath('//svg')
#price_xpaths = driver.find_elements_by_xpath('//svg//g//text')
#price_xpaths = driver.find_elements_by_xpath('//*[@id="PriceAdvisor"]')
#print(price_xpaths)  # always empty list

# single element `object`
svg_item = driver.find_element_by_xpath('//object[@id="PriceAdvisorFrame"]')

# doesn't work - always empty string
#print(svg_item.get_attribute('innerHTML'))

# get url to file SVG
svg_url = svg_item.get_attribute('data')
print(svg_url)  

# download it and parse
r = requests.get(svg_url)
soup = BeautifulSoup(r.content, 'html.parser')

text_items = soup.find_all('text')
for item  in text_items:
    print(item.text)
