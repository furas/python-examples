#!/usr/bin/env python3 

# date: 2020.01.03
# https://stackoverflow.com/questions/59577693/collect-the-dropdown-list-from-link-using-request/

import requests
import lxml.html

url = 'https://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument=OPTIDX&symbol=BANKNIFTY&date=9JAN2020'

r = requests.get(url)
soup = lxml.html.fromstring(r.text)

items = soup.xpath('//form[@id="ocForm"]//option/text()')
#items = [x.text for x in items]
print(items)



