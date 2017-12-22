from selenium import webdriver;import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

def get_data(driver, csv_writer):

    for item in driver.find_elements_by_css_selector(".review-article"):
        name = item.find_elements_by_css_selector("p a")[0].text
        location = item.find_elements_by_css_selector("p")[1].text
        review_date = item.find_elements_by_css_selector("small")[0].text
        review_title = item.find_elements_by_css_selector("strong  a[id^=ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews]")[0].text
        review_data = item.find_elements_by_css_selector(".reviewdata")
        review_data = ' '.join([' '.join(items.text.split()) for items in review_data])
        
        print("Name:", name)
        print("Location:", location)
        print("Review_date:", review_date)
        print("Review_Title:", review_title)
        print("Review_Data:", review_data)
        
        row = [name, location, review_date, review_title, review_data]
        csv_writer.writerow(row)
    
# --- init ---

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/etc/firefox'

driver = webdriver.Firefox(capabilities=firefox_capabilities)
url = "http://www.mouthshut.com/mobile-operators/Reliance-Jio-reviews-925812061"

# --- open file ---

f = open("index.csv", "w")
csv_writer = csv.writer(f)

columns = ["Name", "Location", "Review_data", "Review_title", "Review_data"]
csv_writer.writerow(columns)

# ---- get data ---

print('url:', url)

driver.get(url)
wait = WebDriverWait(driver, 10)

get_data(driver, csv_writer)

# --- get next url ---

url = driver.find_element_by_xpath('//li[@class="next"]/a').get_attribute("href")
   
# ---- get data ---

print('url:', url)

driver.get(url)
wait = WebDriverWait(driver, 10)

get_data(driver, csv_writer)

# --- end ---

driver.quit()
f.close()
