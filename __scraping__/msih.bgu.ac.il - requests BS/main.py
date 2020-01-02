#!/usr/bin/env python3 

# date: 2020.01.02
# ???

import urllib.request
import bs4 as bs

sauce = urllib.request.urlopen('https://msih.bgu.ac.il/md-program/residency-placements/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

headers = soup.find_all('div', class_={'accord-head'})
grad_yr_list = []
for header in headers:
    grad_yr_list.append(header.h2.text[-4:])

rez_classes = soup.find_all('div', class_={'accord-con'})

data_dict = dict(zip(grad_yr_list, rez_classes))

for key, value in data_dict.items():
    print(type(value), key, value.find('h4').text)

