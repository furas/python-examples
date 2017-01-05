#!/usr/bin/env python3

'''
It disable Button if text in Entry was submitted before
'''

import tkinter as tk

# --- functions ---

def submit(event=None):
    data = e.get()

    if data in already_submitted:
        print('Sorry already submitted:', data)
    else:
        print('Submiting:', data)
        already_submitted.append(data)
        b['state'] = 'disable'

def check(event):
    #data = event.widget.get()
    data = e.get()
    if data in already_submitted:
        b['state'] = 'disable'
    else:
        b['state'] = 'normal'

# --- main ---

# don't submit empty string
already_submitted = ['']

root = tk.Tk()

e = tk.Entry(root)
e.pack()
e.bind('<Return>', submit)
e.bind('<KeyRelease>', check)

b = tk.Button(root, text="Submit", command=submit, state='disable')
b.pack()

root.mainloop()
