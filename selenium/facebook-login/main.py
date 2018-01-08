import selenium.webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import pdfkit
#import time
#import webbrowser

LOGIN = 'your_login'
PASSWORD = 'your_password'

driver = selenium.webdriver.Chrome()
#driver = selenium.webdriver.Firefox()
#settings = dict(DesiredCapabilities.PHANTOMJS)
#settings["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36") 
#driver = selenium.webdriver.PhantomJS(desired_capabilities=settings)
#driver.set_window_size(1920, 1200)

driver.get('https://www.facebook.com/login.php')
#time.sleep(1)

driver.find_element_by_id('email').send_keys(LOGIN)
driver.find_element_by_id('pass').send_keys(PASSWORD)
driver.find_element_by_id('loginbutton').click()
#time.sleep(2)

driver.save_screenshot('output.png')
#webbrowser.open('output.png')

#print(driver.page_source)
#pdfkit.from_string(driver.page_source, '/home/furas/file.pdf')

