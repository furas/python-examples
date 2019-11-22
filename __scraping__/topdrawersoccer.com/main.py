#!/usr/bin/env python3

# date: 2019.10.29
# 

import pandas as pd

max_page_num = 15
max_page_dig = 1 # number of digits in the page number

with open('result.csv',"w", newline='') as f:
    f.write("Name, Gender, State, Position, Grad, Club/HS, Rating, Commitment\n")

for i in range(max_page_num):  
   print('page:', i)

   page_num = str(i)
   source = "https://www.topdrawersoccer.com/search/?query=&divisionId=&genderId=m&graduationYear=2020&positionId=0&playerRating=&stateId=All&pageNo=" + page_num + "&area=commitments"

   df = pd.read_html(source)[0]
   print(len(df))
   df.to_csv('results.csv', header=False, index=False, mode='a') #'a' should append each table to the csv file, instead of overwriting it.
