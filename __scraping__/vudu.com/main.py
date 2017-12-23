
#
# https://stackoverflow.com/a/47898209/1832058
# 

from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "https://www.vudu.com/"

#chromedriver = 'C:\\chromedriver.exe'
#browser = webdriver.Chrome(chromedriver)
browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)

print('--- Selenium ---')

all_images = browser.find_elements_by_css_selector('.border .gwt-Image')
for image in all_images[:5]: # first five elements
    #print('image:', image.get_attribute('src'))
    print('alt:', image.get_attribute('alt'))

print('--- BeautifulSoup ---')

soup = BeautifulSoup(browser.page_source, 'html.parser')

all_images = soup.select('.border .gwt-Image')
for image in all_images[:5]: # first five elements
    #print('image:', image['src'])
    print('alt:', image['alt'])
