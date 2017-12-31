import threading
import tkinter as tk
from tkinter import messagebox
import time
import queue


def running(queue):
    
    for x in range(5):
        text = 'message ' + str(x)
        print('put:', text)
        queue.put(text)
        time.sleep(3)
    queue.put('last')

def check_queue():
    
    text = ''
    
    if not queue.empty():
        text = queue.get()
        print('get:', text)
        #messagebox.showinfo(text, text)
        l['text'] = text
    else:
        print('get: - empty -')
        
    if text != 'last':
        root.after(100, check_queue)

# --- main ---

queue = queue.Queue()

t = threading.Thread(target=running, args=(queue,))
t.start()
    
root = tk.Tk()

l = tk.Label(root, text='', width=15, height=2)
l.pack()

tk.Button(root, text='Button 1', width=15, height=2).pack()
tk.Button(root, text='Button 2', width=15, height=2).pack()
tk.Button(root, text='Button 3', width=15, height=2).pack()

check_queue()

root.mainloop()
