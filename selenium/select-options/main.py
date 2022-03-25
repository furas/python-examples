# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.18
# [python - Select nested form - Stack Overflow](https://stackoverflow.com/questions/71522332/select-nested-form/)

# https://selenium-python.readthedocs.io/navigating.html#filling-in-forms

html = '''
<select>
    <optgroup label="FreeMail">
        <option value="option98">gmx.de</option>
        <option value="option99">gmx.net</option>
        <option value="option100">mein.gmx</option>
    </optgroup>
    <optgroup label="ProMail">
        <option value="option101">email.gmx</option>
        <option value="option102">gmx.biz</option>
        <option value="option103">gmx.com</option>
        <option value="option104">gmx.eu</option>
        <option value="option105">gmx.info</option>
        <option value="option106">gmx.org</option>
        <option value="option107">mail.gmx</option>
    </optgroup>
</select>
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("data:text/html;charset=utf-8," + html)

time.sleep(2)

form = driver.find_element(By.XPATH, '//select')

s = Select(form)

print('--- option106 ---')

s.select_by_value('option106')
print('value:', s.first_selected_option.get_attribute('value'))
print('text :', s.first_selected_option.text)

print('--- gmx.org ---')

s.select_by_visible_text('gmx.org')
print('value:', s.first_selected_option.get_attribute('value'))
print('text :', s.first_selected_option.text)


