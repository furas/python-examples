#!/usr/bin/env python3

# date: 2020.06.10
# https://stackoverflow.com/questions/62306522/scraping-list-of-values-from-drop-down/

from selenium import webdriver
from selenium.webdriver.support.ui import Select

#browser = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
browser = webdriver.Firefox()

url = ('https://www.goodjobsfirst.org/violation-tracker')
browser.get(url)
browser.maximize_window()

frame = browser.find_element_by_tag_name("iframe")
print('frame:', frame)

browser.switch_to.frame(frame)

element = browser.find_element_by_id("edit-field-violation-parent-value")
print('element:', element)

select = Select(select)
print('options number:', len(select.options))

for number, item in enumerate(select.options, 1):
    print(number, item.text)

# go back to main content
#browser.switch_to.default_content()

browser.quit()
