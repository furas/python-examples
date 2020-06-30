#!/usr/bin/env python3

# date: 2020.02.26
# https://stackoverflow.com/questions/60405929/python-beautifulsoup-adding-words-from-an-html-paragraph-tag-to-list

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/") 

soup = BeautifulSoup(page.content, "html.parser")
para = soup.find(class_="field-item even")

second_p = para.find_all('p')[1]
text = second_p.text.replace('\t', '')
words = text.split('\n')
print(words)

