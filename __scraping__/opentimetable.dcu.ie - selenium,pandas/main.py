# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.21
# [python - Can not enter course code into timetable, timetable is returning empty - Stack Overflow](https://stackoverflow.com/questions/71205676/can-not-enter-course-code-into-timetable-timetable-is-returning-empty/71206905#71206905)

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import pandas as pd
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(30)

driver.get('https://opentimetable.dcu.ie/')

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_visible_text('Programmes of Study')

search = driver.find_element_by_id("textSearch")
search.send_keys("CASE2")

#checkbox = driver.find_element_by_xpath('.//input[@type="checkbox"]')  # can find wrong `checkbox` - it would need `time.sleep` until it removes other `checkboxes` 
checkbox = driver.find_element_by_xpath('.//input[following-sibling::div[contains(text(), "CASE2")]]')  # it works but it is harder to remeber
#checkbox = driver.find_element_by_xpath('.//div[contains(text(), "CASE2")]')  # it works (in this HTML) and it is simpler to remeber
checkbox.click()

time.sleep(3)

html = driver.find_element_by_id("week-pdf-content").get_attribute('outerHTML')
df2 = pd.read_html(html)[0] 

print(df2.to_string()) # to_string() to display all columns without `...`
