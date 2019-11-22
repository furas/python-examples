
# date: 2019.10.25
# https://stackoverflow.com/questions/58550908/python-click-more-button-is-not-working

#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import selenium

#Incognito Mode
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#Open Chrome
#driver = webdriver.Chrome(executable_path="C:/Users/chromedriver.exe",chrome_options=option)

driver = webdriver.Firefox()

#url I want to visit.
lists = ['https://www.tripadvisor.com/VacationRentalReview-g30196-d6386734-Hot_51st_St_Walk_to_Mueller_2BDR_Modern_sleeps_7-Austin_Texas.html']

for url in lists:

    driver.get(url)
    time.sleep(3)

    link = driver.find_element_by_link_text('More')
    try:
        ActionChains(driver).move_to_element(link)
        time.sleep(1) # time to move to link
        link.click()
        time.sleep(1) # time to update HTML
    except Exception as ex:
        print(ex)

    description = driver.find_element_by_class_name('vr-overview-Overview__propertyDescription--1lhgd')
    print('--- description ---')
    print(description.text)
    print('--- end ---')

    # first "More" shows text in all reviews - there is no need to search other "More"
    first_entry = driver.find_element_by_class_name('entry')
    more = first_entry.find_element_by_tag_name('span')
    try:
        ActionChains(driver).move_to_element(more)
        time.sleep(1) # time to move to link
        more.click()
        time.sleep(1) # time to update HTML
    except Exception as ex:
        print(ex)
        
    all_reviews = driver.find_elements_by_class_name('partial_entry')
    print('all_reviews:', len(all_reviews))
    
    for i, review in enumerate(all_reviews, 1):
        print('--- review', i, '---')
        print(review.text)
        print('--- end ---')
