import requests
import pandas as pd

url = 'https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/statistics/byathlete?region=us&lang=en&contentorigin=espn&isqualified=false&limit=50&category=offense%3Arushing&sort=rushing.rushingYards%3Adesc&season=2018&seasontype=2&page='

df = pd.DataFrame()

for page in range(1, 5):
    print('page:', page)

    r = requests.get(url + str(page))
    data = r.json()

    for item in data['athletes']:
        player_name = item['athlete']['displayName']
        position = item['athlete']['position']['abbreviation']
        gp = item['categories'][0]['totals'][0]
        other_values = item['categories'][2]['totals']
        row = [player_name, position, gp] + other_values

        df = df.append( [row] ) # append one row

df.columns = ['NAME', 'POS', 'GP', 'ATT', 'YDS', 'AVG', 'LNG', 'BIG', 'TD', 'YDS/G', 'FUM', 'LST', 'FD']
print(df.head(20))
