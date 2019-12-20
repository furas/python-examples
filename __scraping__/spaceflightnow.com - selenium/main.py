#!/usr/bin/env python3 

# date: 2019.12.17
# 

import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_links(driver, url):
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source,"lxml")

    links = []
    
    for new_url in soup.find_all('a', href=True):
         new_url = new_url.get('href')
         new_url = urljoin(url, new_url) 
         links.append(new_url)
         
    return links

# ---

options = Options()
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--profile-directory=Default")
#driver = webdriver.Chrome("./chromedriver",options=options)
driver = webdriver.Firefox()

# ---

domain = 'https://spaceflightnow.com/' # to filter external links
start_url = 'https://spaceflightnow.com/'
max_level = 2

links_visited = set([start_url])  # to test visited links
links_with_levels = [(start_url, 0)] # to control levels

# ---

for link, level in links_with_levels:
    if level >= max_level:
        print('skip:', level, link)
        continue

    print('visit:', level, link)

    links = get_links(driver, link)

    print('found:', len(links))
    links = list(set(links) - links_visited)
    print('after filtering:', len(links))
          
    level += 1

    for new_link in links:
        if new_link.startswith(domain): # filter external links
            links_visited.add(new_link)
            links_with_levels.append( (new_link, level) )

# ---

for link, level in links_with_levels:
    print('skip:', level, link)


