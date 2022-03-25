# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.17
# [r - Rvest: using css selector pulls data from different tab in URL - Stack Overflow](https://stackoverflow.com/questions/71515076/rvest-using-css-selector-pulls-data-from-different-tab-in-url/71519294#71519294)

import requests

url = 'https://projects.fivethirtyeight.com/soccer-predictions/forecasts/2021_premier-league_matches.json'

response = requests.get(url)
data = response.json()

for item in data:
    if item['datetime'].startswith('2022-03-16'):
        print('team1:', item['team1_code'], '|', item['team1'])
        print('prob1:', item['prob1'])
        print('score1:', item['score1'])
        print('adj_score1:', item['adj_score1'])
        print('chances1:', item['chances1'])
        print('moves1:', item['moves1'])
        print('---')
        print('team2:', item['team2_code'], '|', item['team2'])
        print('prob2:', item['prob2'])
        print('score2:', item['score2'])
        print('adj_score2:', item['adj_score2'])
        print('chances2:', item['chances2'])
        print('moves2:', item['moves2'])

        print('----------------------------------------')

