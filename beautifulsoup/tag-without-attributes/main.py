#!/usr/bin/env python3

# date: 2019.11.07
# 

from bs4 import BeautifulSoup as BS

text = '<p class="A">text A</p> <p>text B</p> <p id="C">text C</p> <p data="D">text D</p>'

soup = BS(text, 'html.parser')

# --- without class and id
# `class` is reserved keyword so BS uses `class_`

all_items = soup.find_all('p', class_=False, id=False)

for item in all_items:
    print(item.text)

# --- without class and id

all_items = soup.find_all('p', {'class': False, 'id': False})

for item in all_items:
    print(item.text)

# --- without any attributes

all_items = soup.find_all('p')

for item in all_items:
    if not item.attrs:
        print(item.text)

