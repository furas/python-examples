#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59003700/pythonon-ajax-php-prase-result-is-different-from-on-screen-result

import requests

url = 'http://std.stheadline.com/daily/ajax/ajaxFormerly.php'

params = {
    'startDate': '2019-11-20',
    'endDate': '2019-11-22',
    'type[]': '15',
    'keyword': '',
}

r = requests.post(url, data=params)

data = r.json()

print(data['totalCount']) # 47

import pandas as pd
import io

f = io.StringIO(r.text)
df = pd.read_json(f)

print(df)
