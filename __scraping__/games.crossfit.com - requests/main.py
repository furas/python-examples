#!/usr/bin/env python3

# date: 2019.12.20
# https://stackoverflow.com/questions/59419682/how-do-i-extract-this-entire-table-and-store-it-in-csv-file/

import requests

r = requests.get('https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0')

data = r.json()

for row in data['leaderboardRows']:
    print(row['entrant']['competitorName'], row['overallScore'], [(x['rank'],x['scoreDisplay']) for x in row['scores']])
