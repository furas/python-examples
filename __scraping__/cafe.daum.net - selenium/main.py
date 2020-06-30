#!/usr/bin/env python3

# date: 2020.02.23
# https://stackoverflow.com/questions/60362610/python-selenium-click-a-button/

import selenium.webdriver

url = 'http://cafe.daum.net/WekiMeki'

driver = selenium.webdriver.Chrome()
#driver = selenium.webdriver.Firefox()
driver.get(url)

frame = driver.find_element_by_id('down')
driver.switch_to.frame(frame)

driver.find_element_by_id('fancafe-widget-cheer').click()

#driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div/div/section/div/a').click()
