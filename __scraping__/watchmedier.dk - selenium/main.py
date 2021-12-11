
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.03
#
# title: Extract information from table with muliple pages with selenium in Python
# url: https://stackoverflow.com/questions/70217784/extract-information-from-table-with-muliple-pages-with-selenium-in-python/70220956#70220956

# [Extract information from table with muliple pages with selenium in Python](https://stackoverflow.com/questions/70217784/extract-information-from-table-with-muliple-pages-with-selenium-in-python/70220956#70220956)

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open website
#os.environ['PATH'] += r"C:\Users\BackUp HDL\AppData\Local\Programs"
#driver = webdriver.Chrome()
driver = webdriver.Firefox()

# --- accept (but it works also without acceptation) --

print('Load main page')

url = "https://watchmedier.dk/"
driver.get(url)

# Accept cookies
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='SP Consent Message']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Accepter']"))).click()
driver.switch_to.parent_frame()

# --- before loops ---

url = "https://watchmedier.dk/latest/filtered?sitesFilter=policywatch.dk&sitesFilter=shippingwatch.dk&sitesFilter=mobilitywatch.dk&sitesFilter=energiwatch.dk&sitesFilter=finanswatch.dk&sitesFilter=ejendomswatch.dk&sitesFilter=mediawatch.dk&sitesFilter=agriwatch.dk&sitesFilter=fodevarewatch.dk&sitesFilter=medwatch.dk&sitesFilter=kapwatch.dk&sitesFilter=itwatch.dk&sitesFilter=ctwatch.dk&sitesFilter=watchmedier.dk&sitesFilter=advokatwatch.dk&startDate=&endDate="

# load first page - if you use `while`-loop
driver.get(url)

all_results = []

# --- loops ---

page = 1

while True:
#for page in range(1, 4):
    print('--- page:', page, '---')
    
    # load page - if you use `for`-loop
    #driver.get(url + "&pageNumber=" + str(page))
               
    # get all rows in table
    all_rows = driver.find_elements_by_xpath('//table[@class="c-latest-news__table"]//tr')
    
    # process all rows except first with headers
    for number, row in enumerate(all_rows[1:], 1):
        
        #print('row:', number)
        print('.', end='')
        
        # get all columns in row - relative xpath 
        all_cells = row.find_elements_by_xpath('.//td')
        
        date = all_cells[0].text
        
        artikel = all_cells[1].find_element_by_xpath('.//a')
        artikel_text = artikel.text
        artikel_link = artikel.get_attribute('href')
        
        # count `span` and convert to `boolean` (`bool(0)` gives `False`)
        key = bool(len(all_cells[2].find_elements_by_xpath('.//span')))
        
        side = all_cells[3].text
        
        # put row data in list
        all_results.append( [date, artikel_text, artikel_link, key, side] )
        
    print() 
    
    # find button to next page
    try:
        driver.find_element_by_xpath('//button[@onclick]').click()
        page += 1
    except Exception as ex:
        print('Exception:', ex)
        break
    
# --- after loops ---

import pandas as pd

# convert all data to DataFrame
df = pd.DataFrame(all_results, columns=['Dato', 'Artikel text', 'Artikel link', 'Key', 'Side'])

print(df.to_string())

