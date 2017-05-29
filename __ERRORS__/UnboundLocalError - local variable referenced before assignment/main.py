#!/usr/bin/env python3

#
# UnboundLocalError: local variable 'result' referenced before assignment
#
# it is happend only inside function/method
#

import traceback

def example1():
    print(result)
    result = 5
    
def example2a():
    result += 5
        
def example2b():
    result = result + 5
        
def example3():
    '''
    - to create variable `result` you have to assign value,
    - to get value you have to calculate `1/0`
    - but it give exception "division by zero"
    - so it can't give value which you could use to create variable `result`
    - so it doesn't create variable
    - but later it tries to use it - print it
    - and it gives error "UnboundLocalError: local variable 'result' referenced before assignment"
    '''
    
    try:
        result = 1/0
    except Exception as ex:
        print(ex)
    print(result)

def example4():
    if False:
        result = 5
    print(result)

#----------------------------------------------------------------------

examples = [example1, example2a, example2b, example3, example4]


for function in examples:
    print('\n===== Example:', function.__name__, '=====')
    try:
        function()
    #except:
    #except Exception as ex:
    except UnboundLocalError as ex:
        print('\nException:', ex)
        print('\n---\n')
        traceback.print_exc()
