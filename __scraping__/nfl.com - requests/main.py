#!/usr/bin/env python3

import requests

url = 'https://api.nfl.com/v3/shield/?query=%20query%20%7B%20viewer%20%7B%20standings(first%3A1%2CorderBy%3Aweek__weekValue%2CorderByDirection%3ADESC%2Cweek_seasonValue%3A2016%2Cweek_seasonType%3AREG%2C)%20%7B%20edges%20%7B%20cursor%20node%20%7B%20id%20teamRecords%20%7B%20conference%20division%20teamId%20fullName%20nickName%20overallWin%20overallLoss%20overallTie%20overallPct%20overallPtsFor%20overallPtsAgainst%20homeWin%20homeLoss%20homeTie%20homePct%20roadWin%20roadLoss%20roadTie%20roadPct%20divisionWin%20divisionLoss%20divisionTie%20divisionPct%20divisionRank%20conferenceWin%20conferenceLoss%20conferenceTie%20conferencePct%20conferenceRank%20overallStreak%20last5Win%20last5Loss%20last5Tie%20last5Pct%20clinchDivision%20clinchDivisionAndHomefield%20clinchPlayoff%20clinchWc%20%7D%20%7D%20%7D%20%7D%20%7D%20%7D&variables=null'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOiIiLCJjbGllbnRJZCI6InlMTGJjWnpRakFvQ0FtdWF6dUZLR3ZPbkZRS2d5Y0l2IiwiYWRJZCI6bnVsbCwiZXhwIjoxNTE0NjIzNzcwLCJpYXQiOjE1MTQ2MjAxNzB9.kCWZW9h4AaHQUSRHZH7XxGrnRPwajacxE1DF8uROSaA',
    'content-type': 'application/json'
}

r = requests.get(url, headers=headers)

print('--- json ---')
data = r.json()
print('keys:', data['data']['viewer']['standings']['edges'][0]['cursor'])
print('keys:', data['data']['viewer']['standings']['edges'][0]['node']['id'])

print('--- keys ---')

for key in data['data']['viewer']['standings']['edges'][0]['node']['teamRecords'][0].keys():
    print('key:', key)
    
print('--- groups ---')

groups = {}

for item in data['data']['viewer']['standings']['edges'][0]['node']['teamRecords']:
    #print('---')
    #for key, val in item.items():
    #    print(key, val)

    division = item['division']
    fullName = item['fullName']
    
    if division not in groups:
        groups[division] = []
    
    groups[division].append(fullName)
    
for key, val in groups.items():
    print('>>>', key, '<<<')
    for item in val:
        print(' ', item)
