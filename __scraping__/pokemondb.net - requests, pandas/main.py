#!/usr/bin/env python3

# author: https://blog.furas.pl
# date: 2020.07.08
# 

import requests
import pandas as pd

url = "https://www.pokemondb.net/pokedex/all"
html = requests.get(url)

dfs = pd.read_html(html.text)

print( dfs )

