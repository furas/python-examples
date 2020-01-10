#!/usr/bin/env python3 

from blessings import Terminal

t = Terminal()

print(t.bold('Hi there!'))
print(t.bold_red + 'Hi there!')
print(t.bold_red_on_bright_green('It hurts my eyes!'))

with t.location(t.width//2, t.height - 1):
    print('This is at the bottom.')
    
BW  = t.bold_white
BR  = t.bold_red
BG  = t.bold_green
BY  = t.bold_yellow
BB  = t.bold_blue
BC  = t.bold_cyan
RST = t.normal

print(BR + '[DEBUG]: ' + RST + 'ABC')
print(BR('[DEBUG]:') + ' ABC')
print(BR('[DEBUG]:'), 'ABC')
print(BR('[DEBUG]:'), BW('ABC'))
print(BR('[DEBUG]:'), BG('ABC'))
print(BR('[DEBUG]:'), BY('ABC'))
print(BR('[DEBUG]:'), BB('ABC'))
print(BR('[DEBUG]:'), BC('ABC'))

