#!/usr/bin/env python3

# date: 2020.01.06
# https://stackoverflow.com/questions/59604135/how-can-i-store-the-mouse-position-when-it-is-pressed-and-when-it-is-released

from pynput import mouse

pressed_x = 0
pressed_y = 0

released_x = 0
released_y = 0

is_pressed = False
is_released = False

def on_click(x, y, button, pressed):
    global pressed_x
    global pressed_y

    global released_x
    global released_y

    global is_pressed
    global is_released

    # store in external variables
    if pressed:
        is_pressed = True
        pressed_x = x
        pressed_y = y
        #print('LISTENER: pressed:', pressed_x, pressed_y)
    else:        
        is_released = True
        released_x = x
        released_y = y
        #print('LISTENER: released:', released_x, released_y)

    #if not pressed:
    #    # Stop listener
    #    return False

# --- main ---

# start listener at the beginning
listener = mouse.Listener(on_click=on_click)
listener.start()

# use variables in your code
while True:
    if is_pressed:
        print('RUN: pressed:', pressed_x, pressed_y)
        is_pressed = False
    if is_released:
        print('RUN: released:', released_x, released_y)
        is_released = False

# stop listener at the end
listener.stop()            
listener.join()

print('END: pressed:', pressed_x, pressed_y)
print('END: released:', released_x, released_y)
