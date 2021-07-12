
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.07.10
#
# title: Scrapping Market Data
# url: https://stackoverflow.com/questions/68329390/scrapping-market-data/68329695#68329695

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def getData(url):
    
    #driver = webdriver.Chrome(
    #    executable_path='C:/Users/denni/OneDrive/Desktop/DextoolScrapper/app/chromedriver.exe'
    #    )
    
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    
    driver.get('https://www.dextools.io/app/uniswap/pair-explorer/0xa29fe6ef9592b5d408cca961d0fb9b1faf497d6d')

    page = 0

    all_results = []  # list for all rows
    
    while True:

        page += 1
        print('--- page:', page, '---')
        
        # get table
        tableElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ngx-datatable'))
        )
        # scroll into table view
        driver.execute_script("arguments[0].scrollIntoView();", tableElement)
    
        # scrolling through the table body to the bottom
        tableBodyelement = tableElement.find_element_by_tag_name('datatable-body-cell')
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", tableBodyelement)
    
        rowWrapper = tableElement.find_elements_by_tag_name('datatable-row-wrapper')
    
        for row in rowWrapper:
            cells = row.find_elements_by_tag_name('datatable-body-cell')
            date = cells[0].text
            type = cells[1].text
            price_usd = cells[2].text
            price_eth = cells[3].text
            ammount_cuminu = cells[4].text
            total_eth = cells[5].text
            maker = cells[6].find_element_by_tag_name('a').get_attribute('href')
            print(date, type, price_usd, price_eth, ammount_cuminu, total_eth, maker)
            print('----')
            
            # add row to list
            all_results.append( [date, type, price_usd, price_eth, ammount_cuminu, total_eth, maker] )
                                 
    
        try:
            next_page = driver.find_element_by_xpath('//a[@aria-label="go to next page"]')
            next_page.click()
            time.sleep(0.5)
        except Exception as ex:
            print("last page???")
            break
        
    # after loop convert to DataFrame and write it to excel
    
    import pandas as pd
    
    df = pd.DataFrame(all_results, columns=['date', 'type', 'price_usd', 'price_eth', 'ammount_cuminu', 'total_eth', 'maker'])
    df.to_excel('results.xlsx')
    
# ---
 
getData(None)

