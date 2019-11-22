#!/usr/bin/env python3 

# date: 2019.11.22
# https://stackoverflow.com/questions/58997147/how-to-extract-particular-part-of-li-tag-and-omit-span-tag-inside-of-that-l

from bs4 import BeautifulSoup
import requests

headers = {'X-Requested-With': 'XMLHttpRequest'}

r = requests.get('https://www.governmentjobs.com/careers/home/index?agency=sdcounty&sort=PositionTitle&isDescendingSort=false&_=', headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

all_jobs  = soup.find_all('li', attrs = {'class':'list-item'})

for job in all_jobs:
    salary = job.find_all('li')
    text = salary[1].get_text(strip=True)
    text = re.findall('\$[0-9,.]+ - \$[0-9,.]+', text)
    print(text[0])
    
