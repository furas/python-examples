#!/usr/bin/env python3

#
# https://stackoverflow.com/a/47940659/1832058
#

from bs4 import BeautifulSoup
import requests

link = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag"

req = requests.get(link)
web = req.text
soup = BeautifulSoup(web, "lxml")

cve_name = []
cve_link = []

for par_ in soup.find(class_='list_list').find_all('div', attrs={'class':'fl'}):
    print(len(par_))
    for link_ in par_.find_all('p'):
        for text_ in link_.find_all('a'):
            print (text_.string)
            print (text_['href'])
            print ("==========")
            #cve_name.append(text_.string)
            #cve_link.append(text_['href'])
