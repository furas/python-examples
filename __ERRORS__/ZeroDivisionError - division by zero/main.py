#!/usr/bin/env python3

#
# ZeroDivisionError: division by zero
#

import traceback

def example1():
    1/0

def example2():
    a = 1
    b = 0
    
    a/b

def example3():    
    data = []
    
    print('sum:', sum(data))
    print('len:', len(data))
    
    average = sum(data)/len(data)

#----------------------------------------------------------------------

examples = [example1, example2, example3]


for function in examples:
    print('\n--- Example:', function.__name__, '---')
    try:
        function()
    #except:
    #except Exception as ex:
    except ZeroDivisionError as ex:
        print('Exception:', ex)
        print()
        traceback.print_exc()
