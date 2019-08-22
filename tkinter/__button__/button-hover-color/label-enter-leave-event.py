
# date: 2019.08.15

'''button hover color using Label with Enter/Leave events'''

import tkinter as tk

# --- functions ---

def hover_on(event=None):
    print('hover on')
    button['background'] = 'red'

def hover_off(event=None):
    print('hover off')
    button['background'] = standard_bg

# --- main ---    
root = tk.Tk()

button = tk.Label(root, text='Enter/Leave event on Label', relief='raised')
button.pack(fill='x', ipady=5, ipadx=5, pady=1, padx=1)
button.bind('<Button-1>', lambda event:root.destroy())
button.bind('<Enter>', hover_on)
button.bind('<Leave>', hover_off)
standard_bg = button['background']

root.mainloop()
