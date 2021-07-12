from selenium import webdriver
             
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

url = "https://advanced.name/freeproxy"
driver.get(url)

while True:

    print('--- page ---')

    all_ips = driver.find_elements_by_xpath('//td[@data-ip]')
    all_ports = driver.find_elements_by_xpath('//td[@data-port]')
    for ip, port in zip(all_ips, all_ports):
        print(ip.text, port.text)

    try:
        # go to next page
        link_to_next_page = driver.find_element_by_link_text('»')
        link_to_next_page.click()
    except:
        # exit loop if there is no more pages
        break
