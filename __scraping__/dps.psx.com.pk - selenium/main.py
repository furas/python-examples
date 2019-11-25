#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59008770/want-to-read-a-tag-data-using-selenium

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://dps.psx.com.pk/')

last_table = driver.find_elements_by_xpath("//table")[-1]

for row in last_table.find_elements_by_xpath(".//tr")[1:]:
    print(row.find_element_by_xpath(".//td/a[@class='tbl__symbol']").text)
    print([td.text for td in row.find_elements_by_xpath(".//td[@class='right']")])
