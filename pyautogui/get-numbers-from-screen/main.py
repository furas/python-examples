#!/usr/bin/env python3

import pyautogui

def find(screenshot):

    # dictionary for digits grouped by "y"
    
    found = dict()

    # find all digits 
    
    for digit in range(10):
        
        positions = pyautogui.locateAll('digits/{}.png'.format(digit), screenshot, True)
        
        for x,y,_,_ in positions:
            if y not in found:
                found[y] = dict()
            found[y][x] = digit

    # recreate values 

    result = []
    
    for row in sorted(found):
        cols = sorted(found[row])
        value = ''.join(str(found[row][col]) for col in cols)
        result.append(value)
        
    return result

if __name__ == '__main__':
    
    #img = pyautogui.screenshot(region=(0, 0, 300, 400))
    img = 'screenshot-example.png'

    result = find(img)
    
    print('\n'.join(result))
