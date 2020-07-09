from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

try:
    #driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    url = driver.get("http://automationpractice.com/index.php")
    #driver.maximize_window()
    
    search_text_box = driver.find_element_by_id("search_query_top")
    
    search_text_box.send_keys("Printed")
    time.sleep(1) # page display (and update) autocompletion when you make little longer delay 
    
    # --- select using arrow key ---
    
    # move selection on list and accept it
    #search_text_box.send_keys(Keys.ARROW_DOWN)
    #search_text_box.send_keys(Keys.ARROW_DOWN)
    #search_text_box.send_keys(Keys.ARROW_DOWN)
    #search_text_box.send_keys(Keys.ENTER)
    
    # OR
    
    # --- select using tag `<li>` and `text()` in autocompletion --- 
    
    # click on first matching item on list
    #one_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'Dress')]")))
    one_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ac_results']//li[contains(text(),'Dress')]")))
    
    print(' tag:', one_option.tag_name)
    print('text:', one_option.text)
    print('bold:', one_option.find_element_by_xpath('.//strong').text)
    
    one_option.click()

    # OR

    # --- get all elements in autocompletion using `<li>` tag --- 

    # get many matching items and use [index] to click on some item on list
    #one_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'Dress')]")))
    #all_options = driver.find_elements_by_xpath("//li[contains(text(),'Dress')]")
    #for option in all_options:
    #    print(option.tag_name, ':', option.text)
    #all_options[1].click()
    
    print(' current:', driver.current_url)
    print('expected:', "http://automationpractice.com/index.php?id_product=3&controller=product")
    print('the same:', driver.current_url == "http://automationpractice.com/index.php?id_product=3&controller=product")

    assert "http://automationpractice.com/index.php?id_product=3&controller=product" == driver.current_url, "This Test case is fallied"
    #assertEqual("http://automationpractice.com/index.php?id_product=3&controller=product", self.driver.current_url, "This Test case is fallied")
    
except NoSuchElementException as e:
     print('NoSuchElementException:', e)
except TimeoutException as e:
     print('TimeoutException:', e)
except AssertionError as e:
     print('AssertionError:', e)
     
