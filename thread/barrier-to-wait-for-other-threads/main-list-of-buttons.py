#!/usr/bin/env python3 

# date: 2019.12.18
# https://stackoverflow.com/questions/59387309/multithreading-in-python-selenium/59389866#59387309

# it runs 5 browsers, fill forms and wait for other thread to click 'login' button at the same time.

import time
from selenium import webdriver
from threading import Thread

def func(number):
    driver = webdriver.Chrome()
    #driver.set_window_size(920, 680)
    driver.get(url)

    driver.find_element_by_id("email").send_keys("xx")
    driver.find_element_by_id("pass").send_keys("yy")
    b = driver.find_element_by_id("loginbutton")

    buttons[number] = True
    print(buttons)

    # wait for other buttons
    while not all(buttons):
        pass

    print('click', number)
    b.click()

# ---

url = 'https://www.facebook.com/'

number_of_threads = 5

#buttons = [False * number_of_threads] # create place 
buttons = []

threads = []

for number in range(number_of_threads):
    t = Thread(target=func, args=(number,)) # get number for place in list `buttons`
    t.start()
    threads.append(t)
    buttons.append(False) # create place 

for t in threads:
    t.join()
