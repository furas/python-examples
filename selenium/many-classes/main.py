from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

#login = driver.find_element_class_name('js-username-field.email-input.js-initial-focus') # with dots between classes but without dot at the beginning 
#login = driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus') # with dots between classes and dot at the beginning
login = driver.find_element_by_xpath('//*[@class="js-username-field email-input js-initial-focus"]') # without dots - only spaces
login.send_keys("hello")

password = driver.find_element_by_class_name("js-password-field")
password.send_keys("hello")

#button = driver.find_element_class_name('submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium') # with dots between classes but without dot at the beginning 
#button = driver.find_element_css_selector('.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium') # with dots between classes and dot at the beginning
button = driver.find_element_by_xpath('//*[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]') # without dots - only spaces
button.click()
