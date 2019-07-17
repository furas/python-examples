
# date: 2019.07.09
# https://stackoverflow.com/questions/56951383/tkinter-disable-buttons-while-thread-is-running/56953613#56953613

import tkinter as tk
from threading import Thread
import time

def long_running_function():
    print('start sleep')
    time.sleep(3)
    print('end sleep')

def start_thread():
    global t
    global counter
    
    b['state'] = 'disable'
    counter = 0
    
    t = Thread(target=long_running_function)
    t.start()
    
    check_thread()
    # or check after 100ms
    # root.after(100, check_thread) 

def check_thread():
    global counter

    if not t.is_alive():
        b['state'] = 'normal'
        l['text'] = ''
    else:
        l['text'] = '{:.1f}'.format(counter)
        counter += 0.1
        
        # check again after 100ms
        root.after(100, check_thread) 
        
#-----------------------------------------------------

# counter displayed when thread is running        
counter = 0

root = tk.Tk()

l = tk.Label(root)
l.pack()

b = tk.Button(root, text="Start", command=start_thread)
b.pack()

root.mainloop()
