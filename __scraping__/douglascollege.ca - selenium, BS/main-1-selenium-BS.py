
# author: https://blog.furas.pl
# date: 2020.07.09
# https://stackoverflow.com/questions/62805708/how-can-i-get-a-data-from-specific-text-in-div-class-using-a-beautifulsoup/

import selenium.webdriver
from bs4 import BeautifulSoup

url = "https://www.douglascollege.ca/programs-courses/catalogue/programs"

driver = selenium.webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

all_div = soup.find_all("div", class_='ui-accordion-content')

for div in all_div:
    all_items = div.find_all("a")

    for item in all_items:
        print(item.text)
