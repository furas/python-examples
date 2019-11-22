import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get('http://blog.furas.pl')

item = driver.find_element_by_tag_name('title')

print(item.get_attribute('outerHTML'))
print(item.get_attribute('innerHTML'))

