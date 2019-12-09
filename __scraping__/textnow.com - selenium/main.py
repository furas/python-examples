#!/usr/bin/env python3 

# date: 2019.12.08
# https://stackoverflow.com/questions/59238605/finding-page-element-using-seleniumpython

import selenium.webdriver
        
url = 'https://www.textnow.com/login'

driver = selenium.webdriver.Firefox()
driver.get(url)

item = driver.find_element_by_xpath('//input[@id="txt-username"]')
item.send_keys('your_login')

item = driver.find_element_by_xpath('//input[@id="txt-password"]')
item.send_keys('your_password')

item = driver.find_element_by_xpath('//button[@id="btn-login"]')
item.click()
