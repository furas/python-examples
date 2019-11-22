#!/usr/bin/env python3

import tkinter as tk
import time # to simulate long running code
def start():
    text = entry.get()
    print('text:', text)            
    
    label['text'] = 'Running...'
    root.update() # force mainloop to update window
    
    # run some long running code
    time.sleep(3)
    
    label['text'] = 'End'
    root.update() # force mainloop to update window
    
# --- main ---

root = tk.Tk()

label = tk.Label(root, text='Put some text below')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Start', command=start)
button.pack()

root.mainloop()

