#!/usr/bin/env python3 

# date: 2020.01.01
# https://stackoverflow.com/questions/59551193/i-want-to-download-images-from-python-what-should-i-do/

from selenium import webdriver
import requests

#path = r"C:\Users\qpslt\Desktop\py\chromedriver_win32\chromedriver.exe"
#driver = webdriver.Chrome(path)
driver = webdriver.Firefox()

url = "https://gall.dcinside.com/board/view/?id=baseball_new8&no=10131338&exception_mode=recommend&page=1"
driver.get(url)

images = driver.find_elements_by_xpath('//div[@class="writing_view_box"]//img')

for i, img in enumerate(images, 1):
    img_url = img.get_attribute('src')
    print(i, img_url)

    r = requests.get(img_url, headers={'Referer': url})

    with open("c:/test/{}.jpg".format(i), 'wb') as f:
        f.write(r.content)

