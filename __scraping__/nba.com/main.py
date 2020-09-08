#!/usr/bin/env python3 

# date: 2019.11.19, 
# https://stackoverflow.com/questions/58938589/python-scrape-nba-tracking-drives-data
# date: 2020.08.15

import requests

headers = {
    'User-Agent': 'Mozilla/5.0',
    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Referer': 'https://stats.nba.com/players/drives/',
    #'Accept': 'application/json, text/plain, */*',

    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
}

url = 'https://stats.nba.com/stats/leaguedashptstats'

params = {
    'College': '',
    'Conference': '',
    'Country': '',
    'DateFrom': '',
    'DateTo': '',
    'Division': '',
    'DraftPick': '',
    'DraftYear': '',
    'GameScope': '',
    'Height': '',
    'LastNGames': '0',
    'LeagueID': '00',
    'Location': '',
    'Month': '0',
    'OpponentTeamID': '0',
    'Outcome': '',
    'PORound': '0',
    'PerMode': 'PerGame',
    'PlayerExperience': '',
    'PlayerOrTeam': 'Player',
    'PlayerPosition': '',
    'PtMeasureType': 'Drives',
    'Season': '2019-20',
    'SeasonSegment': '',
    'SeasonType': 'Regular Season',
    'StarterBench': '',
    'TeamID': '0',
    'VsConference': '',
    'VsDivision': '',
    'Weight': '',
}

r = requests.get(url, headers=headers, params=params)
#print(r.request.url)
data = r.json()

print(data)
