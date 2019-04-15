import selenium.webdriver

url = "https://www.claytoncountyga.gov/government/sheriff/inmate-search"
driver = selenium.webdriver.Firefox()
driver.get(url)

iframes = driver.find_elements_by_tag_name('iframe')
print('iframes:', iframes)

driver.switch_to.frame(iframes[0])

item = driver.find_element_by_id('name')
print('name:', item)
item.send_keys("John")

item = driver.find_element_by_name('NameSearch')
print('name:', item)
item.click()

