#!/usr/bin/env python3 

# date: 2019.12.18
# https://stackoverflow.com/questions/59386434/selenium-webdriver-i-want-to-click-on-the-next-page-till-last-page/59387563#59387563

from selenium import webdriver
#from bs4 import BeautifulSoup as bs
import time

url = 'https://curecity.in/vendor-list.php?category=Doctor&filters_location=Jaipur&filters%5Bsubareas_global%5D=&filters_speciality='

#driver = webdriver.Chrome('C:\chromedriver.exe')
driver = webdriver.Firefox()
driver.maximize_window()

driver.get(url)
next_page_number = 1

while True:

    print('page:', next_page_number)
    time.sleep(10) # page loads very slow so I need longer sleep

    #soup = bs(driver.page_source, 'html.parser')
    #for link in soup.find_all('div',class_='col-md-9 feature-info'):
    #    link1 = link.find('a')
    #    print(link1['href'])

    for link in driver.find_elements_by_xpath('//div[@class="col-md-2 feature-icon"]/a'):
        print(link.get_attribute('href'))

    try:
        # button '>' jums 3 pages so I click button with number of next page.
        next_page_number += 1
        driver.find_element_by_xpath('//a[@data-page="{}"]'.format(next_page_number)).click()
    except:
        print('No more pages')
        break # exit loop

#driver.close()
