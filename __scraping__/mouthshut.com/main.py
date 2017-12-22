from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from selenium import webdriver;import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

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

driver.get(url)
wait = WebDriverWait(driver, 10)

soup = BeautifulSoup(driver.page_source, "lxml")
for items in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".review-article"))):
   link = items.find_element_by_css_selector(".reviewdata a")
   link.click()
   time.sleep(2)
   
soup = BeautifulSoup(driver.page_source, "lxml")

for item in soup.select(".review-article"):
    name = item.select("p a")[0].text
    location = item.select("p")[1].text
    review_date = item.select("small")[0].text
    review_title = item.select("strong  a[id^=ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews]")[0].text
    review_data = ' '.join([' '.join(items.text.split()) for items in item.select(".reviewdata")])
    
    print("Name:", name)
    print("Location:", location)
    print("Review_date:", review_date)
    print("Review_Title:", review_title)
    print("Review_Data:", review_data)
    
    row = [name, location, review_date, review_title, review_data]
    csv_writer.writerow(row)

# --- get next url ---

uclient = uReq(url)
page_html = uclient.read()
uclient.close()

soup = BeautifulSoup(page_html, "html.parser")
container = soup.find("ul", {"class": "pages table"})

all_li = container.findAll("li")
if all_li:
    last_div = all_li[-1]
    content = last_div.getText()
    content = int(content)
    container = soup.findAll("li", {"class": "next"})
    li = container[0].find("a", {"class": "btn btn-link"}).attrs['href']
   
# ---- get data ---

driver.get(li)
wait = WebDriverWait(driver, 10)

soup = BeautifulSoup(driver.page_source, "lxml")
for items in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".review-article"))):
    link = items.find_element_by_css_selector(".reviewdata a")
    link.click()
    time.sleep(2)

soup = BeautifulSoup(driver.page_source, "lxml")
for item in soup.select(".review-article"):
    name = item.select("p a")[0].text
    location = item.select("p")[1].text
    review_date = item.select("small")[0].text
    review_title = item.select("strong a[id^=ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews]")[0].text
    review_data = ' '.join([' '.join(items.text.split()) for items in item.select(".reviewdata")])

    print("Name:", name)
    print("Location:", location)
    print("Review_date:", review_date)
    print("Review_Title:", review_title)
    print("Review_Data:", review_data)
    
    row = [name, location, review_date, review_title, review_data]
    csv_writer.writerow(row)

# --- end ---

driver.quit()
f.close()
