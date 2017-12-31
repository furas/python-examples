import tkinter as tk

# -----

import subprocess

def callback1():
    cmd = 'python test.py'

    # it will execute script which runs only `function1`
    output = subprocess.check_output(cmd, shell=True)

    lbl['text'] = output.strip()

# -----

class StdoutRedirector(object):
    
    def __init__(self):
        # clear before get all values
        self.result = ''
        
    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.result += text
        
def callback2():
    
    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout
    
    # redirect to class which has `self.result`
    sys.stdout = StdoutRedirector()

    # it will execute only `function2`
    test.function2()

    # assign result to label (after removing ending "\n")
    lbl['text'] = sys.stdout.result.strip()

    # set back original `sys.stdout
    sys.stdout = old_stdout

# -----

import sys

class StdoutRedirectorLabel(object):
    
    def __init__(self, widget):
        self.widget = widget
        # clear at start because it will use +=
        self.widget['text'] = ''
        
    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.widget['text'] += text
        
def callback3():
    
    import test

    # keep original `sys.stdout
    old_stdout = sys.stdout
    
    # redirect to class which will add text to `lbl`
    sys.stdout = StdoutRedirectorLabel(lbl)

    # it will execute only `function3` and assign result to Label (with ending "\n")
    test.function3()

    # set back original `sys.stdout
    sys.stdout = old_stdout

# --- main ---

master = tk.Tk()
master.geometry('200x200')

lbl = tk.Label(master, text='')
lbl.pack()

btn1 = tk.Button(master, text="subprocess", command=callback1)
btn1.pack()

btn2 = tk.Button(master, text="StdoutRedirector", command=callback2)
btn2.pack()

btn3 = tk.Button(master, text="StdoutRedirectorLabel", command=callback3)
btn3.pack()

master.mainloop()
