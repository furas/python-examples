from selenium import webdriver
import time

url = 'https://www.bestbuy.com/site/promo/health-fitness-deals'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(2)

# page "Hello! Choose a Country" - selecting Unitet State flag
driver.find_element_by_class_name('us-link').click()

items = []

for page in range(1, 11):

    print('\n[DEBUG] wait 15 seconds to update page\n')
    time.sleep(15)

    print('\n--- page', page, '---\n')

    all_links = driver.find_elements_by_css_selector('#main-results h4 a')
    for a in all_links:
        link = a.get_attribute("href")
        name = a.get_attribute('text')
        items.append( [name, link] )
        print(name)

    print('\n[DEBUG] load next url\n')
    driver.get(url + '?cp=' + str(page+1) )

    if driver.title == 'Best Buy: Page Not Found':
        break
    
#print(items)
