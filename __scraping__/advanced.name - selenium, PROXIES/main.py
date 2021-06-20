
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.19
#
# title: Python requests-html, trying to load all info in Jscript
# url: https://stackoverflow.com/questions/68042696/python-requests-html-trying-to-load-all-info-in-jscript/

from selenium import webdriver
             
url = "https://advanced.name/freeproxy"

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(url)

all_ips = driver.find_elements_by_xpath('//td[@data-ip]')
all_ports = driver.find_elements_by_xpath('//td[@data-port]')
for ip, port in zip(all_ips, all_ports):
    print(ip.text, port.text)

