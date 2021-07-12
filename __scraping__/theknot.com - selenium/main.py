
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.08
#
# title: How to select option in dropdown using Selenium in Python (Jupyter Notebook)
# url: https://stackoverflow.com/questions/68307222/how-to-select-option-in-dropdown-using-selenium-in-python-jupyter-notebook

from selenium import webdriver
             
url = 'https://www.theknot.com/registry/couplesearch'

driver = webdriver.Firefox()
#driver = webdriver.Chrome()

driver.get(url)

year_dropdown = driver.find_element_by_id("couples-search-year")
year_dropdown.click()

year = year_dropdown.find_element_by_xpath(".//li[contains(text(), '2021')]")
#year = typetextyear.find_element_by_xpath(".//li[text()='2021']")
year.click()

