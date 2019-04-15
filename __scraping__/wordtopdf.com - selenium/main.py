
# date: 2019.04.09
# https://stackoverflow.com/questions/55595886/uploading-file-using-python-selenium-system-via-system-window/55599493#55599493

import selenium.webdriver

your_file = "/home/furas/file.doc"
your_email = "furas@tlen.pl"

url = 'https://www.wordtopdf.com/'
driver = selenium.webdriver.Firefox()
driver.get(url)

# it opens system window for uploading file
#driver.find_element_by_id('file-uploader').click()

file_input = driver.find_element_by_xpath('//input[@type="file"]')
file_input.send_keys(your_file)

email_input = driver.find_element_by_xpath('//input[@name="email"]')
email_input.send_keys(your_email)

driver.find_element_by_id('convert_now').click()


