#!/usr/bin/env python3

# date: 2019.08.12
# https://stackoverflow.com/questions/57454154/pyquery-wont-return-elements-on-a-page
# https://github.com/gawel/pyquery/issues/199

import requests
from pyquery import PyQuery

url = "http://www.floridaleagueofcities.com/widgets/cityofficials?CityID=101"
page = requests.get(url)

pq = PyQuery(page.text, parser="html")
for item in pq('li p'):
    print(item.text)

