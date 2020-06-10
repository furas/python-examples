#!/usr/bin/env python3

import tkinter as tk
import sys

# date: 2019.10.22

# --- classes ---

class Redirect():

    def __init__(self, output):
        self.output = output
        
    def write(self, text):
        self.output.insert('end', text)
        #self.output.see('end')
        
    def flush(self):
        pass
    
# --- main ---
    
root = tk.Tk()

text_output = tk.Text(root)
text_output.pack()

# keep original `stdout` and assing class `Redirect`
old_stdout = sys.stdout
redirect = Redirect(text_output)
#sys.stdout = redirect

# write some text to new output
for x in range(100):
    print("Line:", x, file=redirect)

# write to console 
#old_stdout.write('Hello World!\n')
#print('Hello World!', file=old_stdout)

root.mainloop()

# assign back original `stdout` 
sys.stdout = old_stdout

