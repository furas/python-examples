#!/usr/bin/env python3 

# date: 2019.11.22
# https://stackoverflow.com/questions/58997147/how-to-extract-particular-part-of-li-tag-and-omit-span-tag-inside-of-that-l

from bs4 import BeautifulSoup
import requests

headers = {'X-Requested-With': 'XMLHttpRequest'}

r = requests.get('https://www.governmentjobs.com/careers/home/index?agency=sdcounty&sort=PositionTitle&isDescendingSort=false&_=', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')
all_jobs  = soup.find_all('li', attrs = {'class':'list-item'}) # gives container with all we need

for job in all_jobs:
    salary = job.find_all('li')
    text = salary[1].get_text(strip=True)
    text = '$' + text.split('$', 1)[1]
    text = ' '.join(text.split(' ')[:3])
    print(text)

