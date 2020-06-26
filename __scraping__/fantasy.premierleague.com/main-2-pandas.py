# https://stackoverflow.com/questions/62521126/table-web-scraping-issues-with-python/

from urllib.request import urlopen
import json
import pandas as pd

#url = 'https://fantasy.premierleague.com/player-list'
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

# read data from url and convert to Python's list/dictionary
text = urlopen(url).read().decode()
data = json.loads(text)

# create DataFrames
players = pd.DataFrame.from_dict(data['elements'])
teams   = pd.DataFrame.from_dict(data['teams'])

# divide by 10 to get `6.2` instead of `62`
players['now_cost'] = players['now_cost'] / 10

# convert team's number to its name
players['team'] = players['team'].apply(lambda x: teams.iloc[x-1]['name'])

# filter players
goalkeepers = players[ players['element_type'] == 1 ]
defenders   = players[ players['element_type'] == 2 ]
# etc.

# some informations
print('\n--- goalkeepers columns ---\n')

print(goalkeepers.columns)

print('\n--- goalkeepers sorted by name ---\n')

sorted_data = goalkeepers.sort_values(['first_name'])

print(sorted_data[['first_name', 'team', 'now_cost', 'yellow_cards', 'red_cards']].head())

print('\n--- goalkeepers sorted by cost ---\n')

sorted_data = goalkeepers.sort_values(['now_cost'], ascending=False)

print(sorted_data[['first_name', 'team', 'now_cost', 'yellow_cards', 'red_cards']].head())

print('\n--- teams columns ---\n')

print(teams.columns)

print('\n--- teams columns ---\n')

print(teams['name'].head())

# etc.

