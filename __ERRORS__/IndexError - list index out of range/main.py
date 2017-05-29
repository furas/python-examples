#!/usr/bin/env python3

#
# IndexError: list index out of range
#

import traceback

def example1a():
    a = []
    b = a[0]

def example1b():
    a = [1,2,3]
    b = a[10]

def example2a():
    a = []
    a[0] += 1

def example2b():
    a = [1,2,3]
    a[10] += 1
    
    
#----------------------------------------------------------------------

examples = [example1a, example1b, example2a, example2b]


for function in examples:
    print('\n--- Example:', function.__name__, '---')
    try:
        function()
    #except:
    #except Exception as ex:
    except IndexError as ex:
        print('\nException:', ex)
        print('\n---\n')
        traceback.print_exc()
