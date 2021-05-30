#!/usr/bin/env python3

# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.04.26
# https://stackoverflow.com/questions/67254893/scraping-text-of-class-with-selenium-and-with-whitespaces-between-different-text/


from selenium import webdriver

#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver = webdriver.Edge()

driver.get('https://www.fussballdaten.de/vereine/fc-bayern-muenchen/2019/')

# close popup window with message
driver.find_element_by_xpath('//button[@aria-label="Einwilligen"]').click()

print('--- FIND ---')

dots_graph = driver.find_element_by_class_name("tore-dots")
all_items = dots_graph.find_elements_by_tag_name("text")

dot_vals = [item.text for item in all_items]
print(dot_vals)

print('--- XPATH 1 ---')

# doesn't work with `g` and `text` - maybe because it is inside `<SVG>` 
all_items = driver.find_elements_by_xpath('//g[@class="tore-dots"]//text')  

dot_vals = [item.text for item in all_items]
print(dot_vals)

print('--- XPATH (*, name) ---')

all_items = driver.find_elements_by_xpath('//*[@class="tore-dots"]//*[local-name()="text"]')

dot_vals = [item.text for item in all_items]
print(dot_vals)

print('--- XPATH (*, local-name) ---')

all_items = driver.find_elements_by_xpath('//*[@class="tore-dots"]//*[name()="text"]')

dot_vals = [item.text for item in all_items]
print(dot_vals)

print('--- CSS ---')

all_items = driver.find_elements_by_css_selector('.tore-dots text')

dot_vals = [item.text for item in all_items]
print(dot_vals)

