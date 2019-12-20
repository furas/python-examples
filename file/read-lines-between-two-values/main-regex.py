#!/usr/bin/env python3 

text = '''DATA_out file
      values
    DATA_LINE 1
    DATA_LINE 2
    DATA_LINE 3
    DATA_LINE 4
total
'''

import re

#result = re.search('values(.*)total', text, re.DOTALL)
#result = re.search('values\n(.*)\ntotal', text, re.DOTALL)
#result = re.search('values[^\n]*\n(.*)\n[^\n]*total', text, re.DOTALL)

if result:
    print(result[1])
    #print(result.group(1))    

