#!/usr/bin/env python3 

# date: 2019.12.14

a= """
   ###
   # #
   ###
   # #
   # #
   """

b= """
   ###
   # #
   ###
   # #
   ###
   """

SPACE = """
       
       
       
    
      
    """

a = a.splitlines()
b = b.splitlines()
SPACE = SPACE.splitlines()
word = [a,b,SPACE,b,a]

for lines in zip(*word):
    print(' '.join(x[-3:] for x in lines))
    

