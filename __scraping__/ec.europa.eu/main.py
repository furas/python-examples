#!/usr/bin/env python3

# date: 2020.01.10
# https://stackoverflow.com/questions/59674921/how-can-i-scrape-image-url-from-this-website/

import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()

url = 'https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_consultation.jsp?Lang=en&Lang=en&refcountry=&reference=&valstartdate=&valstartdateto=&valenddate=&valenddateto=&suppldate=&nomenc=3824&nomencto=&keywordsearch1=&keywordsearch=&specialkeyword=&keywordmatchrule=OR&descript=&orderby=4&Expand=true&offset=1&viewVal=Thumbnail&isVisitedRef=false&allRecords=0&showProgressBar=true'
r = s.get(url)

url = 'https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_list.jsp?viewVal=Thumbnail&Lang=en&offset=1&allRecords=0&nomenc=3824&orderby=4&keywordmatchrule=OR&isVisitedRef=false&random=8377162'
r = s.get(url)
soup = BS(r.text, 'html.parser')

all_items = soup.find_all('img')
for item in all_items:
    print(item['src'])
 
