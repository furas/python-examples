# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.22
# [python - How to save a list of lists as csv - Stack Overflow](https://stackoverflow.com/questions/73079431/how-to-save-a-list-of-lists-as-csv/)

from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.rotowire.com/soccer/lineups.php?league=MLS').text
soup = BeautifulSoup(html_text, 'html.parser')
lineups = soup.find_all('div', class_='lineup is-soccer')

# --- before loop ---

all_results = []

# --- loop ---

for selection in lineups[:2]:
    home_squad = selection.find('ul', class_='lineup__list is-home')
    home_players = home_squad.find_all('li', class_='lineup__player')
    for home_player in home_players[:4]:
        h_player_name = home_player.find('a').text
        all_results.append(h_player_name)

# --- after loop ---

df_h = pd.DataFrame(all_results)
df_h.to_csv('home.csv', index=False, header=False)

