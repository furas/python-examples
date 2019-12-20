#!/usr/bin/env python3 

# date: 2019.12.11
# https://stackoverflow.com/questions/59262263/how-to-keep-track-of-mouse-events-and-position-using-selenium-and-javascript-in/

import selenium.webdriver
import time

url = 'https://stackoverflow.com'
driver = selenium.webdriver.Firefox()
driver.get(url)

driver.execute_script('window.x = null;')

driver.execute_script('document.body.addEventListener("click", function(e) { window.x = e.target;})')

while True:
    print(driver.execute_script('window.y = window.x; window.x = null; return window.y'))
    time.sleep(.5)

