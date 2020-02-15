#!/usr/bin/env python3

# date: 2020.02.11

import selenium.webdriver
from selenium.webdriver.common.keys import Keys 

driver = selenium.webdriver.Firefox()
driver.get('https://google.com')

item = driver.find_element_by_name('q')
item.send_keys(Keys.CONTROL + "v")

