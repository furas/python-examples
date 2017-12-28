
#
# https://stackoverflow.com/a/47990190/1832058
#

import tkinter as tk

'''
It lets you input only numbers 8.2 digits.

'''
def check(d, i, P, s, S, v, V, W):
    print("d='%s'" % d)
    print("i='%s'" % i)
    print("P='%s'" % P)
    print("s='%s'" % s)
    print("S='%s'" % S)
    print("v='%s'" % v)
    print("V='%s'" % V)
    print("W='%s'" % W)    
    
    text = P #e.get()
    print('text:', text)

    parts = text.split('.')
    parts_number = len(parts)

    if parts_number > 2:
        #print('too much dots')
        return False

    if parts_number > 1 and parts[1]: # don't check empty string
        if not parts[1].isdecimal() or len(parts[1]) > 2:
            #print('wrong second part')
            return False

    if parts_number > 0 and parts[0]: # don't check empty string
        if not parts[0].isdecimal() or len(parts[0]) > 8:
            #print('wrong first part')
            return False
        
    return True

# --- main ---

root = tk.Tk()

vcmd = (root.register(check), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

e = tk.Entry(root, validate='key', validatecommand=vcmd)
e.pack()

root.mainloop()
