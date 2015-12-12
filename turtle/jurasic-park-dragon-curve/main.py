#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Dragon_curve
# https://en.wikipedia.org/wiki/L-system

# https://pl.wikipedia.org/wiki/Smok_Heighwaya
# https://pl.wikipedia.org/wiki/L-system

# https://en.wikipedia.org/wiki/Sierpinski_triangle

import turtle

# --- functions ---

def dragon(level=1, remove_plus_minus=False, width=5):

    a = 'FX'

    rule = {
        'X': 'X+YF+',
        'Y': '-FX-Y',
        '-': '-',
        '+': '+',
        'F': 'F',
    }

    for _ in range(level):
        a = ''.join(rule[x] for x in a)

    print('len:', len(a))

    a = a.replace('X', '').replace('Y','')
    print('len without X, Y:', len(a))
    
    if remove_plus_minus:
        a = a.replace('+-', '').replace('-+', '')
        print('len without -+, +-:', len(a))
            
    for x in a:
        if x == 'F':
            turtle.forward(width)
        elif x == '+':        
            turtle.right(90)
            turtle.color('red')
        elif x == '-':
            turtle.left(90)
            turtle.color('green')

    print('OK')
    
# --- main ---

# clear everything
turtle.reset()

# the fastest turtle
turtle.speed(0)

# hide turtle
turtle.hideturtle()


dragon(10, False, 10)


# keep open window
turtle.exitonclick()
