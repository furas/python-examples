# https://stackoverflow.com/questions/62521126/table-web-scraping-issues-with-python/

from urllib.request import urlopen
import json
import pandas as pd

#url = 'https://fantasy.premierleague.com/player-list'
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

text = urlopen(url).read().decode()
data = json.loads(text)

print('\n--- element type ---\n')        

#print(data['element_types'][0])
for item in data['element_types']:
    print(item['id'], item['plural_name'])

print('\n--- Goalkeepers ---\n')        

number = 0

for item in data['elements'][:1]:
        
    if item['element_type'] == 1: # Goalkeepers
        number += 1
        print('---', number, '---')
        print('type        :', data['element_types'][item['element_type']-1]['plural_name'])
        print('first_name  :', item['first_name'])
        print('second_name :', item['second_name'])
        print('total_points:', item['total_points'])
        print('team        :', data['teams'][item['team']-1]['name'])
        print('cost        :', item['now_cost']/10)

        if item['first_name'] == 'Alisson':
            for key, value in item.items():
                print('    ', key, '=',value)

