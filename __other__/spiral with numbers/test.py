#!/usr/bin/env python3

from main import * 

__author__ = 'Mark Geyzer (https://www.facebook.com/Mark.Geyzer)

'''
This is a test harness for a numeric spiral builder
Place your function(s) here and run the harness
'''

def test_funcs(*funcs):
    import traceback
    import re
   
    tests = (
        (1,),
        (1, 2),
        (3, 1, 2),
        (4, 3, 1, 2),
        (5, 4, 3,  1, 2),
        (5, 4, 3, 6, 1, 2, 7, 8),
        (5, 4, 3, 6, 1, 2, 7, 8, 9),
        (5, 4, 3, 6, 1, 2, 7, 8, 9, 10),
        (5, 4, 3, 6, 1, 2, 11, 7, 8, 9, 10),
        (5, 4, 3, 12, 6, 1, 2, 11, 7, 8, 9, 10),
        
        (37, 36, 35, 34, 33, 32, 31,
         38, 17, 16, 15, 14, 13, 30,
         39, 18, 5, 4, 3, 12, 29,
         40, 19, 6, 1, 2, 11, 28,
         41, 20, 7, 8, 9, 10, 27,
         42, 21, 22, 23, 24, 25, 26,
         43, 44, 45, 46, 47, 48, 49),
    )
    for func in funcs:
        print(f'\n\nTesting function {func.__name__}:\n')
        for expected in tests:
            tested_num = max(expected)
            result = str(func(tested_num))
            result = tuple(map(int, re.findall(r'\d+', result)))
            try:
                assert result == expected
            except AssertionError:
                print(f'FAILED for {tested_num}')
                print(f' tested: {result}')
                print(f' expected: {expected}')
            else:
                print(f'Passed for {tested_num}: {result}')
 
 
''' testing functions '''
if __name__ == '__main__':
    func_list = [func for name, func in globals().items()
                 if callable(func) and name[0:2] not in ('__')
                    and name[0:4] not in ('exit', 'quit', 'get_', 'test')]
    test_funcs(*func_list)
