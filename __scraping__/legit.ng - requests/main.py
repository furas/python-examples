#!/usr/bin/env python3

# date: 2020.01.09
# 

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.legit.ng/1087216-igbo-proverbs-meaning.html')
soup = BeautifulSoup(res.content, 'html.parser')

data = []
for div in soup.find_all('div'):
    for block in div.find_all('blockquote'):
        text = block.text
        if text.startswith('Igbo Proverb – '):
            name = text[15:] # len('Igbo Proverb – ') == 15
            data.append(name)

for item in data:
    print(item)
