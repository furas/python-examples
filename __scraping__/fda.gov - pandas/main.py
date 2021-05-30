
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.05.28
#
# title: HTTP Error 400 Bad request calling api with python
# url: https://stackoverflow.com/questions/67730460/http-error-400-bad-request-calling-api-with-python/67740975#67740975

# Based on [documentation](https://open.fda.gov/apis/query-parameters/) 
# you should use `skip` instead of `limit` - and use always `limit=100` 
# like `limit=100&skip=0`, `limit=100&skip=100`, `limit=100&skip=200`, `limit=100&skip=300`, etc.

import pandas as pd

limit = 100
url = 'https://api.fda.gov/drug/ndc.json?search=dea_schedule:"{}"&limit={}&skip={}'
all_data_df = []

for skip in range(0, 2321, 100):
    query = url.format('CII', limitskip)
    print('query:', query)
    data = pd.read_json(query, orient='values', typ='series', convert_dates=False)
    data = data['results']
    all_data_df.append(data)
    
print(all_data_df)

