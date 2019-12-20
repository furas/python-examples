#!/usr/bin/env python3

text = '''DATA_out file
      values
    DATA_LINE 1
    DATA_LINE 2
    DATA_LINE 3
    DATA_LINE 4
total
'''

import io

#f = open("input.txt")
f = io.StringIO(text)

lines = []

# read till you find line with 'values'
for line in f:
    if 'values' in line:
        break

# read till you find line with 'total' and keep lines on list
for line in f:
    if 'total' in line:
        break
    lines.append(line)
else:
    #if not found `total` (so there was no `break`) then clear list
    lines = []    

if lines:
    print("".join(lines))    
