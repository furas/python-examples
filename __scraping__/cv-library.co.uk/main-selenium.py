#!/usr/bin/env python3

from selenium import webdriver

site_url = "https://www.cv-library.co.uk/companies/agencies/0-9"

# --- Opening Firefox with Selenium Webdrivre ---

browser = webdriver.Firefox() 

#I need my Firefox browser's current profile for a reason.
#profile = webdriver.FirefoxProfile(r"C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\i27jf7iw.default")
#browser = webdriver.Firefox(firefox_profile=profile)

browser.get(site_url)

# --- Clicking Phone Buttons ---

phone_btn = browser.find_elements_by_link_text("Phone - Click to View")
for btn in phone_btn:
    btn.click()

numbers = browser.find_elements_by_class_name('company-profile-phone')
for num in numbers:
    print('number:', num.text)
