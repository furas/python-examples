from selenium import webdriver
import time

LOGIN = 'xxx@xxx.com' 
PASSWORD = 'PaSwOrD'

# --- start ---

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

# resize window so all elements are visible 
# and the is no problem to click them 
driver.maximize_window()
#driver.set_window_size(1920, 1080)
#driver.execute_script("window.resizeTo(1920,1080)") # doesn't work for me

# --- main page ---

#driver.get("https://www.myntra.com/")

# --- login ---

driver.get('https://www.myntra.com/login?referer=https://www.myntra.com/')

# sometimes it has problem to login but it seems `sleep()` resolves it.
time.sleep(1)

item = driver.find_element_by_css_selector('.login-user-input-email')
item.send_keys(LOGIN)

item = driver.find_element_by_css_selector('.login-user-input-password')
item.send_keys(PASSWORD)

item = driver.find_element_by_css_selector('.login-login-button')
item.click()

time.sleep(1)

# --- main page ---

#driver.get("https://www.myntra.com/")

# --- cart ---

item = driver.find_element_by_css_selector('.desktop-cart')
item.click()

# or

#driver.get('https://www.myntra.com/checkout/cart')


