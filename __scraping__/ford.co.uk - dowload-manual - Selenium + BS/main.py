

# https://stackoverflow.com/questions/60377798/error-while-selecting-dependent-drop-down-and-click-the-option-in-python/60378558#60378558
# Error while selecting dependent drop down and click the option In Python


# BTW: sometimes page shows popup window at start but I didn't try to solve this problem

# BTW: I had to check `if yearText != 'Year' and modelText != 'Model':` to skip clicks for these values.

#------------------------------------------------------------------------------

url = "https://www.ford.co.uk/owner/my-vehicle/download-your-manual"

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome() #'C:/Users/chromedriver.exe')
driver.get(url)
time.sleep(4)
selectYear = Select(driver.find_element_by_id("odl-selected-year"))

data = []
for yearOption in selectYear.options:
    yearText = yearOption.text
    selectYear.select_by_visible_text(yearText)
    time.sleep(1)

    selectModel = Select(driver.find_element_by_id("odl-selected-model"))
    for modelOption in selectModel.options:
        modelText = modelOption.text
        selectModel.select_by_visible_text(modelText)
        if yearText != 'Year' and modelText != 'Model':
            data.append([yearText, modelText])

            #print(data)

            button = driver.find_element_by_link_text("Select this vehicle")
            button.click()
            time.sleep(2)

            page = driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            content = soup.findAll('a', attrs={"class": "odl-download-link"})

            links =[]
            for i in content:
                links.append(i["href"])

            print(links)

            # go back

            driver.find_element_by_class_name('odl-back-link').click()

