#!/usr/bin/env python3

# date: 2020.01.18
# 

from pandas.io.html import read_html

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

wikitables = read_html(url, index_col=0, attrs={"class":"wikitable plainrowheaders wikiepisodetable"})

print("Extracted {num} wikitables".format(num=len(wikitables)))

for i, dataframe in enumerate(wikitables):
  dataframe.to_csv('file{}.csv'.format(i))
