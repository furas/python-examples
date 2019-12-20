#!/usr/bin/env python3 

# date: 2019.12.14

chars = {
'a':
"""
###
# #
###
# #
# #
""".splitlines()[1:],

'b':
"""
###
# #
###
# #
###
""".splitlines()[1:],

' ': 
"""
   
   
   
   
   
""".splitlines()[1:],
}

word = 'ab ba'
word = [chars[x] for x in word]

for lines in zip(*word):
    print('>', ' '.join(lines), '<')
    

