
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.02.07
# https://stackoverflow.com/questions/66082627/trackingnumber-soup-findinput-name-tracknums-getvalue

from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

# load page with form

driver.get('https://wwwapps.ups.com/WebTracking/OnlineTool')

# accept cookies at start

cookies_option = driver.find_element_by_id('privacy_pref_optin')
cookies_option.click()

cookies_button = driver.find_element_by_id('consent_prompt_submit')
cookies_button.click()

# change tab `Track by Reference`

tab = driver.find_element_by_id('ui-id-3')
tab.click()

# fill form

number = driver.find_element_by_name('ReferenceNumber')
number.send_keys("w83139338")

date_1 = driver.find_element_by_name('FromDatepicker')
date_1.clear()
date_1.send_keys("01.11.2020")  # Polish format
#date_1.send_keys("11/01/2020")  # US format

date_2 = driver.find_element_by_name('ToDatepicker')
date_2.clear()
date_2.send_keys("07.02.2021")  # Polish format
#date_1.send_keys("02/07/2021")  # US format

# press button 

track_button = driver.find_element_by_name('trackref.x')
track_button.click()

# get results

track_number = driver.find_element_by_id('trkNum').text
print('track_number:', track_number)

elements = driver.find_elements_by_xpath('//div[@class="secBody clearfix"]//p')
for item in elements:
    text = item.text
    print('item:', text)

address = driver.find_element_by_xpath('//address/p')
print('address:', address.text)

hidden = driver.find_elements_by_xpath('//form[@name="podForm1"]//input')
for item in hidden:
    name = item.get_attribute('name')
    value = item.get_attribute('value')
    print('hidden:', name, '=', value)

# or use `BeautifulSoup`

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')

# ... code ...

