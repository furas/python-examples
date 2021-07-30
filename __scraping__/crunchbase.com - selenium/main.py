
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.23
#
# title: How to iterate through web table with Selenium?
# url: https://stackoverflow.com/questions/68493382/how-to-iterate-through-web-table-with-selenium/68494220#68494220

# DOESN"T WORK WITH FIREFOX BECAUSE SERVER SHOWS CAPTCHA


from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

#paths
#PATH = "C:/Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

url = "https://www.crunchbase.com/search/organizations/field/organization.companies/categories/electric-vehicle"
driver.get(url)
driver.maximize_window()
time.sleep(5)

print('title:', driver.title)

WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
          (By.XPATH, ('//grid-body//identifier-formatter/a/div/div')
        )))

all_rows = driver.find_elements_by_css_selector("grid-row")

all_companies = []
                          
for row in all_rows:
    company = {
        'name':     row.find_element_by_xpath('.//*[@class="identifier-label"]').text.strip(),
        'industry': row.find_element_by_xpath('.//*[@data-columnid="categories"]//span').text.strip(),
        'hq':       row.find_element_by_xpath('.//*[@data-columnid="location_identifiers"]//span').text.strip(),
    }
    all_companies.append(company)
    
#create dataframe    
df = pd.DataFrame(all_companies)
print(df)
