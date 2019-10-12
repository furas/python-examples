
# date: 2019.09.15
# https://stackoverflow.com/questions/57941221/how-can-i-use-jquery-with-selenium-execute-script-method

from selenium import webdriver
import time

url = 'https://stackoverflow.com/questions/57941221/how-can-i-use-jquery-with-selenium-execute-script-method'
driver = webdriver.Firefox()
driver.get(url)

driver.execute_script("""var jquery_script = document.createElement('script'); 
jquery_script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
jquery_script.onload = function(){var $ = window.jQuery;};
document.getElementsByTagName('head')[0].appendChild(jquery_script);""")

time.sleep(0.5) # time to load jQuery library
#driver.execute_script('$ = window.jQuery;')

driver.execute_script('$("h1").wrap("<i></i>")')
#driver.execute_script('$ = window.jQuery;$("h1").wrap("<i></i>")')
