#!/usr/bin/env python3

# date: 2020.05.23
# https://stackoverflow.com/questions/61976765/can-i-tick-a-checkbox-using-beautifulsoup-selenium/

import selenium.webdriver

url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox'

#driver = selenium.webdriver.Chrome()
driver = selenium.webdriver.Firefox()
driver.get(url)

# checkboxes are in <iframe> so I have to switch frame
driver.switch_to.frame(0)

# click checkboxes using names
for name in ["vehicle1", "vehicle2", "vehicle3"]:
    items = driver.find_element_by_name(name)
    #items = driver.find_element_by_xpath(f'//input[@name="{name}"]')
    items.click()

# click "Submit"
#button = driver.find_element_by_xpath('//input[@type="submit"]')
button = driver.find_element_by_xpath('//input[@value="Submit"]')
button.click()        
