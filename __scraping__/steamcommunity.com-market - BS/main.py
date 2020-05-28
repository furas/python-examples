#!/usr/bin/env python3

# date: 2020.05.28
# https://stackoverflow.com/questions/62056266/steam-market-parsing

from urllib.request import urlopen
from bs4 import BeautifulSoup

link = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Knife&appid=730#p1_price_asc'
page = urlopen(link)

bs_page = BeautifulSoup(page.read(), features="html.parser")
objects = bs_page.findAll(class_="market_listing_row_link")

data = []

for g in objects:
    link  = g["href"]
    price = g.find('span', {'data-price': True})['data-price']
    price = int(price)
    data.append((price,link))
    
data = sorted(data)

print("\n".join(f"${price/100} USD | {link}" for price, link in data))

