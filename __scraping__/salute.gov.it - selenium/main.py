#!/usr/bin/env python3

"""
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2024.04.29
# [While i scrape website, can I search for specific keywords in a searchbar with Selenium (python)? - Stack Overflow](https://stackoverflow.com/questions/78398520/while-i-scrape-website-can-i-search-for-specific-keywords-in-a-searchbar-with-s/78405308#78405308)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time

# ---

import selenium
print('Selenium:', selenium.__version__)

# ---

def scrape_page(driver, keyword):
    try:

        # Gestisci il banner dei cookie, se presente
        try:
            print('Clicking cookie banner')            
            cookie_banner = driver.find_element(By.XPATH, "//a[b[text()='Chiudi']]")
            cookie_banner.click()
        except Exception as e:
            print('Exception:', e)

        # Trova tutti gli elementi "Continua a leggere"
        elements_dt = driver.find_elements(By.CSS_SELECTOR, "dl.simple-list.results dt")
        #elements_dd = driver.find_elements(By.XPATH, "//dl[@class='sample-list.results']/dd/a")
        
        print('[DEBUG] len(elements_dt):', len(elements_dt))
        # Lista per memorizzare i dati estratti
        data = []

        # Clicca su ciascun elemento
        #for index, element_dt, element_dd in enumerate(zip(elements_dt, elements_dd), 1):  # you can use `enumerate(..., 1)` to start `index` with `1`
        for index, element in enumerate(elements_dt, 1):  # you can use `enumerate(..., 1)` to start `index` with `1`
            
            try:
                article_url = element.find_element(By.XPATH, './/a').get_attribute("href")
                article_title = element.text
                
                # ... DON'T CLIK LINKS BECAUSE IT WILL REMOVE CURRENT PAGE FROM MEMPRY
                # ... AND YOU WILL LOST ACCESS TO OTHER `elements` ON CURRENT PAGE
                # ...
                # ... Get `href` and later (after loop) use `.get(href)` to access subpages. 
                
                data.append({
                    'keyword': keyword,
                    'Titolo': article_title, 
                    'URL': article_url, 
                    #'Data': article_date, 
                    #'Contenuto': article_content
                })
                
                print('[DEBUG] data:', data[-1])
                # Torna alla pagina precedente
                #driver.back()
            except Exception as e:
                print("Errore durante il clic sull'elemento:", e)
                
        # work with subpages

        for item in data:
            print('[DEBUG] subpage:', item['URL'])
            driver.get(item['URL'])
            #article_date = ...
            #article_content = ...
            #item['Data'] = article_date
            #item['Contenuto'] = article_content
             
    except Exception as e:
        print("Errore durante lo scraping della pagina:", e)
        return None

    return data

# --- main ---

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# ---

start_url = "https://www.salute.gov.it/portale/home.html"

all_data = []

keywords = ['ukraina', 'covid-19', 'elan musk']

for word in keywords:

    print("Main Page:", start_url)

    # open main page 
    driver.get(start_url)

    # find searchbar
    print('Search:', word)
    searchbar = driver.find_element(By.ID, "f_cerca")
    # put keyword in searchbar and press ENTER
    searchbar.send_keys(word)
    searchbar.send_keys(Keys.ENTER)
    
    time.sleep(5) # wait for results
    
    #get current url (because it could load different URL to show results)
    search_results_url = driver.current_url
    
    # start scraping results (with pagination):
    #while True:  # try to get all pages
    for _ in range(3):  # try to get only 3 pages
        print("Scraping:", search_results_url)
        
        page_data = scrape_page(driver, word)  # <--- only scraping, without `.get(url)`, I send `word` only to add it to `data`
        
        if page_data:
            all_data.extend(page_data)

        driver.get(search_results_url) # go back to result after visiting subpages - to get link to next page 
        
        try:
            next_page_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Successive')]")
            search_results_url = next_page_link.get_attribute("href")
            driver.get(search_results_url)  # <--- open next page with results using URL
            #next_page_link.click()   # <--- or click link 
        except Exception as e:
            print('[DEBUG] Exception:', e)
            print('[DEBUG] break')
            #input('Press ENTER to continue')
            break  # exit loop
            
driver.quit()

import pandas as pd
df = pd.DataFrame(all_data)
print(df)

input("Press ENTER to close")
