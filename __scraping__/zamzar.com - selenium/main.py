import selenium.webdriver
from selenium.webdriver.support.ui import Select
import time

your_file = "/home/furas/Obrazy/37884728_1975437959135477_1313839270464585728_n.jpg"
#your_file = "/home/you/file.jpg"
output_format = 'png'

url = 'https://www.zamzar.com/'
driver = selenium.webdriver.Firefox()
driver.get(url)

#--- file --- 

# it has to wait because paga has to create second `input[@type="file"]`
file_input = driver.find_elements_by_xpath('//input[@type="file"]')
while len(file_input) < 2:
    print('len(file_input):', len(file_input)) 
    time.sleep(0.5)
    file_input = driver.find_elements_by_xpath('//input[@type="file"]')

file_input[1].send_keys(your_file)

#--- format ---

select_input = driver.find_element_by_id('convert-format')      
select = Select(select_input)
select.select_by_visible_text(output_format)

#--- convert ---

driver.find_element_by_id('convert-button').click()

#--- download ---

time.sleep(5)

driver.find_elements_by_xpath('//td[@class="status last"]/a')[0].click()
