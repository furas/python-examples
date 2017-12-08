#!/usr/bin/env python3

import datetime

'''
count number of days between 7.12.2017 and day 9 months earier.
'''

def days(day, month, year, size=9):

    # current date
    start_month = month
    start_year = year
    
    # earlier date
    end_month = start_month - size
    end_year = year
    
    # reacalculate when year change
    if end_month < 1:
        end_year -= 1
        end_month += 12
    
    # get both date
    d1 = datetime.date(year=start_year, month=start_month, day=day)
    d2 = datetime.date(year=end_year, month=end_month, day=day)
    print(d1, d2)
    
    # calculate difference
    result = (d2 - d1).days
    print(result)

# --- main ---

for a in range(1, 12):
    days(7, a, 2017, 9)
