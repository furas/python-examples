
# https://stackoverflow.com/questions/60601053/python-selenium-for-loop-iterates-through-entire-website/60601428

from selenium import webdriver
import time

driver = webdriver.Chrome()

#wait = WebDriverWait(driver, 10)

driver.get("https://www.aopa.org/destinations/airports/state/AL")
time.sleep(3)

airport_list = []
paved_runway = []

airport_row = driver.find_elements_by_xpath('//div[@class = "state-airports__airport"]')
print(len(airport_row))

for r in airport_row:
    #print(r.text)
    airport_list.append(r.text)

    badge = r.find_elements_by_xpath('.//div[@class="airport-icons"]//app-badge')
    if badge:
        print(r.text + ": Y")
        paved_runway.append(r.text + ": Y")
    else:
        print(r.text + ": N")
        paved_runway.append(r.text + ": N")

driver.close()
