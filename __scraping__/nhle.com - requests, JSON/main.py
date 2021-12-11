
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.12.01
#
# title: Scrape for Table with Limits
# url: https://stackoverflow.com/questions/70179298/scrape-for-table-with-limits/70180875#70180875

# [Scrape for Table with Limits](https://stackoverflow.com/questions/70179298/scrape-for-table-with-limits/70180875#70180875)

import requests
import pandas as pd

# --- before loop ---

url = 'https://api.nhle.com/stats/rest/en/team/daysbetweengames'

payload = {
    'isAggregate': 'false',
    'isGame': 'true',
    'start': 0,
    'limit': 100,
    'sort': '[{"property":"teamFullName","direction":"ASC"},{"property":"daysRest","direction":"DESC"},{"property":"teamId","direction":"ASC"}]',
    'factCayenneExp': 'gamesPlayed>=1',
    'cayenneExp': 'gameDate<="2021-11-30 23:59:59" and gameDate>="2021-10-12" and gameTypeId=2',
}

df = pd.DataFrame()

# --- loop ---

for start in range(0, 1000, 100):
    print('--- start:', start, '---')
    
    payload['start'] = start
    
    response = requests.get(url, params=payload)

    data = response.json()

    df = df.append(data['data'], ignore_index=True)
    
# --- after loop ---

print(df)

df.to_excel('Master File.xlsx', sheet_name='Info')

print(df.iloc[0])
print(df.iloc[100])



