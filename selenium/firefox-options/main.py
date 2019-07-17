#!/usr/bin/env python3

# date: 2019.07.11
# https://stackoverflow.com/questions/56991061/why-does-selenium-still-ask-me-to-configure-saves-when-i-have-it-set-in-python-a

import os
from selenium import webdriver

url = 'https://www150.statcan.gc.ca/n1/tbl/csv/' + '10100127' + '-eng.zip'
        
FF_options = webdriver.FirefoxProfile()

FF_options.set_preference("browser.download.dir", os.getcwd()) 
FF_options.set_preference("browser.download.folderList",2)        

FF_options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
#FF_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

#FF_profile.set_preference("browser.download.manager.showWhenStarting", False)

driver= webdriver.Firefox(firefox_profile=FF_options)
driver.get(url)

driver.close()

