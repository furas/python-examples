#!/usr/bin/env python3

'''
See table `Mask/Modifier` on
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-handlers.html
'''

import tkinter as tk

# --- functions ---

def method(event):

    # for `Shift` it gives upper char in `event.char` and `event.keysym`

    print('-----')
    print('[DEBUG] event.char       :', event.char)
    print('[DEBUG] event.keysym     :', event.keysym)
    print('[DEBUG] event.keycode    :', event.keycode)
    print('[DEBUG] event.keysym_num :', event.keysym_num)
    print('[DEBUG] event.state      :', event.state, '=', bin(event.state))
    print('[DEBUG] event.state      :', event.state, '=', bin(event.state))
    print('-----')

    if event.char: # skip Control_L, Shift, but also `Up`, `Down`, etc

        # if you need `& 5` then it has to be before `& 4` and `& 1`

        if event.state & 5 == 5:
            # it needs `== 5` because `& 5` can give results `5`, `4`
            # or `1` which give `True` or `0` which gives `False`
            print('method: Control+Shift +', event.keysym)

        elif event.state & 4:
            # it doesn't need `== 4` because `& 4` can give
            # only `4` or `0`
            print('method: Control +', event.keysym)

        elif event.state & 1:
            # it doesn't need `== 1` because `& 1` can give
            # only  `1` or `0`
            print('method: Shift +', event.keysym)

        else:
            print('method:', event.keysym)

# --- main ---

root = tk.Tk()

root.bind("<Key>", method)

root.mainloop()
