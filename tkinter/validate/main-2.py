import tkinter as tk

#
# https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter/4140988#4140988
#

def convert(text):
    parts = []
    while text:
        parts.insert(0, text[-3:])
        text = text[:-3]
    return '.'.join(parts)

def check(d, i, P, s, S, v, V, W):
    print("d='%s'" % d)
    print("i='%s'" % i)
    print("P='%s'" % P)
    print("s='%s'" % s)
    print("S='%s'" % S)
    print("v='%s'" % v)
    print("V='%s'" % V)
    print("W='%s'" % W)    
    print('-----')
    
    if V == 'focusin':
        print('if focus in')
        text = P

        # remove points of hundreds
        text = text.replace('.', '')

        e.delete('0', 'end')
        e.insert('end', text)
        
        return True
        
    if V == 'focusout':
        print('if focus out')
        text = P
    
        # add points of hundreds
        parts = text.split(',')

        if len(parts) > 0:
            parts[0] = convert(parts[0])
        text = ','.join(parts)

        #e.delete('0', 'end')
        #e.insert('end', text)
        
        return True
        
    if V == 'key':
        print('if key')
        text = P

        # validate    
        parts = text.split(',')
        parts_number = len(parts)
    
        if parts_number > 2:
            print('too much dots')
            return False
    
        if parts_number > 1 and parts[1]: # don't check empty string
            if not parts[1].isdecimal() or len(parts[1]) > 2:
                print('wrong second part')
                return False
    
        if parts_number > 0 and parts[0]: # don't check empty string
            if not parts[0].isdecimal() or len(parts[0]) > 8:
                print('wrong first part')
                return False
            
        return True
    
# --- main ---

root = tk.Tk()

vcmd = (root.register(check), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

e = tk.Entry(root, validate='all', validatecommand=vcmd)
e.pack()

b = tk.Button(root, text='Other widget to set focus')
b.pack()

root.mainloop()
