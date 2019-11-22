#!/usr/bin/env python3

"""
# date: 2019.10.29
# 
"""

import pandas as pd

max_page_num = 15

url = "https://www.topdrawersoccer.com/search/?query=&divisionId=&genderId=m&graduationYear=2020&positionId=0&playerRating=&stateId=All&area=commitments&pageNo={}"

headers = ["Name", "Gender", "State", "Position", "Grad", "Club/HS", "Rating", "Commitment"]

with open('result.csv',"w", newline='') as fh:
    fh.write( ','.join(headers) + '\n' )

for i in range(max_page_num):  
   print('page:', i)

   all_tables = pd.read_html(url.format(i))
   print(len(all_tables))
   df = all_tables[0]

   df.to_csv('results.csv', header=False, index=False, mode='a')  # append each table to the csv file
