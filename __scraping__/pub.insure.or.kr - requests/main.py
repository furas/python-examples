#!/usr/bin/env python3 

# date: 2019.11.26
# https://stackoverflow.com/questions/59043401/i-want-web-crawling-from-ajaxpython

import requests
from bs4 import BeautifulSoup

url = 'https://pub.insure.or.kr/compareDis/variableInsrn/fundDay/fundInfoViewPopup.do?stdYmd=20191125&memberCd=L71&fundCd=KLVL71FD25O'

s = requests.Session() # to keep cookies
r = s.get(url, verify=False) 

params = {
    "fundTabId": "fundSummary",
    "stdYmd": "20191125",
    "memberCd": "L71",
    "fundCd": "KLVL71FD25O"
}

url = 'https://pub.insure.or.kr/compareDis/variableInsrn/fundDay/fundSummaryAjax.do'
r = s.post(url, data=params, verify=False)

#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

all_h3 = soup.find_all('h3')
for item in all_h3:
    print(item.text)
