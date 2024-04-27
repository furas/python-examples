#!/usr/bin/env python3

"""
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2024.04.27
# [python - Selenium returns TimeoutException when I try to enter the email address in a webpage - Stack Overflow](https://stackoverflow.com/questions/78394555/selenium-returns-timeoutexception-when-i-try-to-enter-the-email-address-in-a-web/78395190#78395190)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException
#import time

# ---

import selenium
print('Selenium:', selenium.__version__)

# ---

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

url = "https://careers-se.icims.com/jobs/70145/login?mobile=false&width=1200&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330"
driver.get(url)

driver.implicitly_wait(30)
#time.sleep(30)
#input('Press ENTER to continue')

all_frames = driver.find_elements(By.CSS_SELECTOR, 'iframe')
print('len(all_frames):', len(all_frames))

#frame = driver.find_element(By.CSS_SELECTOR, 'iframe')
frame = all_frames[0]
print(frame)

driver.switch_to.frame(frame)

enter_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='css_loginName']")))

enter_email.clear()
enter_email.send_keys("Hello", Keys.RETURN)

input('Press ENTER to continue')
