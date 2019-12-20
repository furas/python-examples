import selenium.webdriver
        
url = 'https://toscrape.com/'
url = 'http://books.toscrape.com/'

#driver = selenium.webdriver.Firefox()
#driver.get(url)

try:
    item = driver.find_element_by_xpath('//tag').text.strip()
except Exception as ex:
    print(ex)
    item = driver.find_element_by_xpath('//a').text.strip()
print(item)

from bs4 import BeautifulSoup as BS

soup = BS(driver.page_source, 'html.parser')


item = soup.find('tag')
if not item:
    item = soup.find('a')
    if not item:
        item = ''
        
item = item.get_text(strip=True)
print(item)
    
