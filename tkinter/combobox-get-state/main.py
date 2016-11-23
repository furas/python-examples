
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Widget.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-state-spec.html

try:
    # Python 2
    import Tkinter as tk
    import ttk
    print('Python 2')
except:
    # Python 3
    import tkinter as tk
    import tkinter.ttk as ttk
    print('Python 3')

def test():
    all_states = ['disabled', 'readonly', 'pressed', 'focus']

    print('----------------------------------------------------')

    
    c['state'] = tk.NORMAL

    print('   info:', c['state'])
    print('compare:', c['state'] == tk.NORMAL, c.cget('state') == tk.NORMAL)
    print('instate:', c.instate(all_states), all_states)
    print('instate:', c.instate(['disabled']), ['disabled'])
    print('instate:', c.instate(['!disabled']), ['!disabled'])
    print('state():', c.state())
    print('  state:', c.state(all_states))
    #print('  state:', c.state([tk.DISABLED]))
    #print('state():', c.state())

    print('---')
    print('  normal:',   c['state'].string == tk.NORMAL, str(c['state']) == tk.NORMAL)
    print('disabled:', c['state'].string == tk.DISABLED, str(c['state']) == tk.DISABLED)
    print('readable:', c['state'].string == tk.READABLE, str(c['state']) == tk.READABLE)

    print('----------------------------------------------------')

    c['state'] = tk.DISABLED

    print('   info:', c['state'])
    print('compare:', c['state'] == tk.NORMAL, c.cget('state') == tk.NORMAL)
    print('instate:', c.instate(all_states), all_states)
    print('instate:', c.instate(['disabled']), ['disabled'])
    print('instate:', c.instate(['!disabled']), ['!disabled'])
    print('state():', c.state())
    print('  state:', c.state(all_states))
    print('  state:', c.state([tk.DISABLED]))
    print('state():', c.state())

    print('---')
    print('  normal:',   c['state'].string == tk.NORMAL, str(c['state']) == tk.NORMAL)
    print('disabled:', c['state'].string == tk.DISABLED, str(c['state']) == tk.DISABLED)
    print('readable:', c['state'].string == tk.READABLE, str(c['state']) == tk.READABLE)


root = tk.Tk()

c = ttk.Combobox(root)
c.pack()

print('\n=== start ===\n')
test()
#print('\n=== after ===\n')
#root.after(2000, test)

root.mainloop()
