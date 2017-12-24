
#
# https://stackoverflow.com/a/47706550/1832058
#

from selenium import webdriver
import time

driver = webdriver.Chrome("E:\Tutorial\Driver\chromedriver.exe")

words = ['girl', 'cat', 'dog', 'bird', 'man']
for word in words:
    driver.get("https://translate.google.com.eg/?hl=en&tab=wT#en/fr/" + word)
    time.sleep(1)
    try:
        translations = driver.find_elements_by_class_name('gt-baf-word-clickable')

        for text in translations:
            print(text.text)
    except Exception as ex:
        print(ex)
