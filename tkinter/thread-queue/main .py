import threading
import tkinter as tk
from tkinter import messagebox
import time
import queue


def running(queue):
    
    for x in range(5):
        text = 'message ' + str(x)
        print('PUT:', text)
        queue.put(text)
        time.sleep(4)
    queue.put('last')

def check_queue():
    global t
    
    text = ''
    
    if not queue.empty():
        text = queue.get()
        print('get:', text)
        l['text'] = text
    else:
        print('get: - empty -')
        
    if text == 'last':
        t = None
    else:
        root.after(500, check_queue)    
    
def on_click():
    global t
    
    if not t:
        t = threading.Thread(target=running, args=(queue,))
        t.start()
        check_queue()
    else:
        messagebox.showinfo('INFO', 'Process still running')
        
    
# --- main ---

t = None
queue = queue.Queue()
    
root = tk.Tk()

l = tk.Label(root, text='', width=15, height=2)
l.pack()

b = tk.Button(root, text='Start', command=on_click, width=15, height=2)
b.pack()

root.mainloop()
