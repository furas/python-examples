
#
# https://stackoverflow.com/a/47539575/1832058
# 

from selenium import webdriver

browser = webdriver.Chrome() #'/usr/local/bin/chromedriver')

browser.get('https://www.facebook.com/SparColruytGroup/app/300001396778554?app_data=DD722A43-C774-FC01-8823-8016BFF8F0D0')
browser.implicitly_wait(5)

iframe = browser.find_element_by_css_selector('#pagelet_app_runner iframe')
browser.switch_to_frame(iframe)

iframe = browser.find_element_by_css_selector('#qualifio_insert_place iframe')
browser.switch_to_frame(iframe)

button = browser.find_element_by_css_selector('#softGateBox > div.button_softgate > a')
browser.execute_script("arguments[0].scrollIntoView(true);", button)

button.click()
