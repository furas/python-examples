
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.01.05
# https://stackoverflow.com/questions/65573230/i-cant-get-the-webdriver-to-fill-space-with-text-but-ive-tried-everything-on/65573872#65573872

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def order(k):

    email_tab = 2 #Number of times to hit tab for email

    # Load the Driver
    print('main page')

    driver = webdriver.Chrome()
    driver.get(k['product_url'])

    wait = WebDriverWait(driver, 10)

    # Choose the bottle via xpath
    print('bottle page')
    
    #bottle = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="thumb-bbt2020package"]/div/div[1]/div/div/img')))
    bottle = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="thumb-biereblanche"]/div/div[1]/div/div/img')))
    bottle.click()
    
    #Adding the item to the cart
    print('add to cart')

    add_to_cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sqs-add-to-cart-button-inner')))
    add_to_cart.click()
    
    # Going to the cart
    print('go to cart')
    
    enter_cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'custom-cart-button')))
    enter_cart.click()
    
    #print('go to checkout')
    #driver.get(k['checkout_url'])
    
    # OR 
    
    # Going to checkout screen
    print('go to checkout')
    
    # multiple class names need `.` between names
    checkout_cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sqs-editable-button.CheckoutButton-checkoutButton-3yWY2.checkout-button')))                                                                           
    checkout_cart.click()
    
    #Enter the email
    print('email')
    
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * email_tab)
    actions.send_keys('hello@world.com')
    #email_field.send_keys(Keys.ENTER)
    actions.perform()
    
    import time
    time.sleep(3)
    
# --- main ---
    
keys = {
    "product_url": "https://sideprojectbrewing.com/shop?category=Beer+Release", 
    "checkout_url": "https://sideprojectbrewing.com/checkout",
} 

order(keys)
