# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.16
# [javascript - How can I extract an array from the console.log in selenium? - Stack Overflow](https://stackoverflow.com/questions/71502197/how-can-i-extract-an-array-from-the-console-log-in-selenium/71503642#71503642)

# https://xyproblem.info/
# https://en.wikipedia.org/wiki/XY_problem
# https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem


from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

url = 'https://www.highcharts.com/demo/line-basic'

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

time.sleep(5)

data = driver.execute_script('''return Highcharts.charts[0].series[0].data.map(d => d.y);''')

print(type(data), data)

# Result 

'''
<class 'list'> [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
'''
