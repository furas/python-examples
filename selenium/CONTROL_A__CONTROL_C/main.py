#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import pyperclip

driver = webdriver.Firefox()
driver.get("http://quotes.toscrape.com")

element = driver.find_element_by_tag_name("body")

# it gets only visible text.
# it works with <body> but not have to with other tags.
element.send_keys(Keys.CONTROL, "a")
element.send_keys(Keys.CONTROL, "c")
#print(pyperclip.paste()) # text from Clipboard

# it gets all text in HTML 
# ie. country names in <select>
print(element.text)
