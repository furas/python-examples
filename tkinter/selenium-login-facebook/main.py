# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.13
# [python - Problem when I log into Facebook in Tkinter and Selenium, using the textboxes for user and password - Stack Overflow](https://stackoverflow.com/questions/71854285/problem-when-i-log-into-facebook-in-tkinter-and-selenium-using-the-textboxes-fo/)
import os
import tkinter as tk                    
from tkinter import ttk

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# --- functions ---

def login():
    profile_path = '/usr/bin/firefox/firefox'

    options = Options()
    options.set_preference('profile', profile_path)
    options.set_preference('network.proxy.type', 4)
    options.set_preference('network.proxy.socks', '127.0.0.1')
    options.set_preference('network.proxy.socks_port', 9050)
    options.set_preference("network.proxy.socks_remote_dns", False)

    #service = Service('/home/jass/bin/geckodriver')
    service = Service('/home/furas/bin/geckodriver')
    driver = Firefox(service=service, options=options)
    driver.get("https://www.facebook.com")

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cookiebanner="accept_only_essential_button"]'))).click()   

    username_box = driver.find_element(By.ID, 'email')
    username_box.send_keys(email.get())
      
    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(password.get())
      
    login_box = driver.find_element(By.ID, 'loginbutton')
    login_box.click()

# --- main ---

root = tk.Tk()
root.title("Login")
root.geometry('630x500')

topbar = tk.Frame(root, bg='#3c5999', height=42)
topbar.pack(fill='x')

label_email = tk.Label(topbar, text="email", bg='#3c5999', foreground="white")
label_email.place(x=2, y=10)

email = tk.Entry(topbar)
email.place(x=50, y=9)

label_password = tk.Label(topbar, text="password", bg='#3c5999', foreground="white")
label_password.place(x=260, y=10)

password = tk.Entry(topbar)
password.place(x=335, y=9)

button = tk.Button(topbar, text="Login", bg='white', foreground='black', width=7, command=login)
button.place(x=530, y=5)

root.mainloop()
