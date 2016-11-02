#!/usr/bin/env python

try:
    import Tkinter as tk # Python 2.x
except:
    import tkinter as tk # Python 3.x
    
from datetime import datetime

# --- constants ---

    # empty

# --- classes ---

    # empty

# --- functions ---

def update_time():
    # update displayed time
    current_time = datetime.now()
    current_time_str = current_time.strftime('%Y.%m.%d  %H:%M:%S')
    # current_time_str = datetime.now().strftime('%Y.%m.%d  %H:%M:%S')
    
    label['text'] = current_time_str

    # run update_time again after 1000ms (1s)
    root.after(1000, update_time)

# --- main ---

# create main window and set its title
root = tk.Tk()
root.title('Time')

# create variable for displayed time and use it with Label
label = tk.Label(root)
label.pack()

# run update_time first time
update_time()
# or run update_time first time after 1000ms (1s)
# root.after(1000, update_time)

# start the engine :)
root.mainloop()
