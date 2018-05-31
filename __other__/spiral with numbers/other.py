#!/usr/bin/env python3

import math

__author__ = 'Bartłomiej "furas" Burek'


def test_sizes(numbers=26):
    '''Show matrix size and start position for 1..numbers'''

    for value in range(1, numbers+1):
        size = math.ceil(math.sqrt(value))
        print('[TEST] numbers:', value, 'size:', size)


def test_starts(value=6):
    '''Show start position for sizes 1..value'''
    

    for size in range(1, value):
        center = math.floor((size-1) / 2)
        x = center
        y = (size - 1) - center # flip up-down
        print('[TEST] size:', size, 'start:', x, y, '(x,y)')


if __name__ == '__main__':

    test_sizes(26)
    print('---')
    test_starts(6)
    print('---')
