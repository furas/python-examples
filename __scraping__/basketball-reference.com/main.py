
# date: 2019.04.28
# author: Bartłomiej 'furas' Burek
# https://stackoverflow.com/a/55885909/1832058

import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url = 'https://www.basketball-reference.com/players/b/bogutan01.html#advanced::none'

r = requests.get(url)

soup = BeautifulSoup(r.content)

all_comments = soup.find_all(string=lambda text: isinstance(text, Comment))

for item in all_comments:
    if "Advanced" in item:
        adv = BeautifulSoup(item)
        playertr = adv.find("table", id="advanced").find("tbody").findAll("tr")
        playerws = adv.find_all("td")[21].getText()
        #print('playertr:', playertr)
        print('playerws:', playerws)
            for row in playertr:
                if row:
                    print(row.find_all('th')[0].text)
                    all_td = row.find_all('td')
                    print([x.text for x in all_td])
                    print('--')
        break # skip after first comment with "Advanced". Other comments with "Advanced" are not tables.

