#!/usr/bin/env python3

# date: 2020.06.05
# https://stackoverflow.com/questions/62217254/python-tkinter-make-text-widget-automatically-scroll-with-text-used-with-redir/

import tkinter as tk
import sys
import datetime

# --- classes ---

class RedirectText(object):

    def __init__(self, widget):
        """Constructor"""
        self.output = widget

    def write(self, string):
        """Add text to the end and scroll to the end"""
        self.output.insert('end', string)
        self.output.see('end')

    # some widgets may need it if they don't have it
    #def flush(self):
    #    pass
    
# --- functions ---
        
def add_time():
    """Add current time every 2 seconds"""
    print(datetime.datetime.now())
    root.after(2000, add_time)

# --- main ---

root = tk.Tk()

text = tk.Text(root)
text.pack()

button_top = tk.Button(root, text="Move to TOP", command=lambda:text.see('1.0'))
button_top.pack()

button_end = tk.Button(root, text="Move to END", command=lambda:text.see('end'))
button_end.pack()

# keep original `stdout` and assing `RedirectText` as `stdout`
old_stdout = sys.stdout
sys.stdout = RedirectText(text)

# add some datetime at the beginning 
print('--- TOP ---')
for _ in range(50):
    print(datetime.datetime.now())
    
# add new datetime every 2 seconds
add_time()
                   
# write to console when `print()` is redirected to `RedirectText()`
old_stdout.write('Hello World!\n')      # need '\n'
print('Hello World!', file=old_stdout)  # no need '\n'
                                    
root.mainloop()    
    
# assign back original `stdout`    
sys.stdout = old_stdout

