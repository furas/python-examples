
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.06.21
#
# title: Python requests-html, trying to load all info in Jscript
# url: https://stackoverflow.com/questions/68042696/python-requests-html-trying-to-load-all-info-in-jscript/68043295?noredirect=1#comment120295742_68043295

from selenium import webdriver
             
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

url = "https://advanced.name/freeproxy?ddexp4attempt=1&page="
for page in range(15):
    print('--- page', page, '---')
    driver.get(url + str(page))

    all_ips = driver.find_elements_by_xpath('//td[@data-ip]')
    all_ports = driver.find_elements_by_xpath('//td[@data-port]')
    for ip, port in zip(all_ips, all_ports):
        print(ip.text, port.text)

