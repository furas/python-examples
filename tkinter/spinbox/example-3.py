import tkinter as tk

'''
One Spinbox automatically changes other Spinbox 
'''

def sb1_changed(): # first spinbox
    # get selection in first spinbox
    selected = sb1_var.get()
    # find its index on first list of all values
    idx = vals1.index(selected)
    # use index to get value for other list of all values
    val = vals2[idx]
    # set selection in second spinbox
    sb2_var.set(val)

    print('selected/index/val:', selected, idx, val)
    

def sb2_changed(): # second spinbox
    # get selection in first spinbox
    selected = sb2_var.get()
    # find its index on first list of all values
    idx = vals2.index(selected)
    # use index to get value for other list of all values
    val = vals1[idx]
    # set selection in second spinbox
    sb1_var.set(val)

    print('selected/index/val:', selected, idx, val)
    

# ---

'''
sb1['textvariable'] give ID, not object but sb1.get() works
sb1['values'] gives list with values
'''

def changed(sb1, sb2):
    # get selection in first spinbox
    selected = sb1.get()

    # find its index on first list of all values
    idx = sb1['values'].index(selected)  # <- but it works ['values']
    
    # use index to get value for other list of all values
    val = sb2['values'][idx]             # <- but it works ['values']
    
    print('selected/index/val:', selected, idx, val)
    
    # set selection in second spinbox
    sb2.insert('0', val)         # <- problem with ['textvariable']

    print('selected/index/val:', selected, idx, val)
    

# --- main ---

vals1 = ['A', 'B', 'C']
vals2 = ['1', '2', '3']

root = tk.Tk()

sb1_var = tk.StringVar()
sb2_var = tk.StringVar()

sb1 = tk.Spinbox(root, textvariable=sb1_var, values=vals1, command=sb1_changed)
sb1.pack()

sb2 = tk.Spinbox(root, textvariable=sb2_var, values=vals2, command=sb2_changed)
sb2.pack()

# ---

sbA_var = tk.StringVar()
sbB_var = tk.StringVar()

sbA = tk.Spinbox(root, textvariable=sbA_var, values=vals1)
sbA.pack()

sbB = tk.Spinbox(root, textvariable=sbB_var, values=vals2)
sbB.pack()

sbA['command'] = lambda:changed(sbA, sbB)
sbB['command'] = lambda:changed(sbB, sbA)

# ---

root.mainloop()
