from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# --- functions ---

def fill_popup(driver):
    # once opened it will fill in the confirm your age
    day = Select(driver.find_element_by_xpath('//*[@id="bday_day"]'))
    day.select_by_index(2)
    
    month = Select(driver.find_element_by_xpath('//*[@id="bday_month"]'))
    month.select_by_index(4)
    
    year = Select(driver.find_element_by_xpath('//*[@id="bday_year"]'))
    year.select_by_index(24)
    
    province = Select(driver.find_element_by_xpath('//*[@id="province"]'))
    province.select_by_index(5)
    
    button = driver.find_element_by_xpath('//*[@id="popup-subscribe"]/button')
    button.click()

# --- main ---
driver = webdriver.Firefox()
driver.get('https://www.tastyrewards.com/en-ca/contest/fritolaycontest/participate')

# have to go through select your birthday
fill_popup(driver)

# 2 seconds is enough for the website to load
time.sleep(2)

# there are still two "province" in HTML so I has to get second "province"

all_province = driver.find_elements_by_xpath('//*[@id="province"]')
second = all_province[1]

province = Select(second)
province.select_by_index(5)

