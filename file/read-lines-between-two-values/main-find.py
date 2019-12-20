#!/usr/bin/env python3

text = '''DATA_out file
      values
    DATA_LINE 1
    DATA_LINE 2
    DATA_LINE 3
    DATA_LINE 4
total
'''

start = text.find('values')
end = text.find('total', start)

if start > -1 and end > -1:
    start += len("values")  
    print(text[start:end])

