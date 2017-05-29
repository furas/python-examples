#!/usr/bin/env python3

#
# IndexError: list assignment index out of range
#

import traceback

def example1a():
    a = []
    a[0] = 1

def example1b():
    a = [1,2,3]
    a[10] = 1


#----------------------------------------------------------------------

examples = [example1a, example1b]


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
