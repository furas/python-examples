from selenium import webdriver
import time

'''
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''

driver = webdriver.Firefox()
driver.get('http://quotes.toscrape.com//')

time.sleep(2)

print('--- Selenium ---')

tables = driver.find_elements_by_xpath('//span[@class="tag-item"]/a')

for item in tables:
    print('text:', item.text)
    print('href:', item.get_attribute('href'))
    print('-----')
print()    
    
# ---------------------------------------------------------------------

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')

print('--- BeautifulSoup ---')

tables = soup.find_all('span', class_='tag-item')

for item in tables:
    item = item.find('a')
    print('text:', item.text)
    print('href:', item['href'])
    print('-----')
print()    
