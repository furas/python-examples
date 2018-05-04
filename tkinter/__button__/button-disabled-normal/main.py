import tkinter as tk

def callback_1():
    b1['state'] = 'disabled'
    print('state:', b1['state'])
    
def callback_2():
    b1['state'] = 'normal'
    print('state:', b1['state'])
    
    
root = tk.Tk()

b1 = tk.Button(root, text='Disable', command=callback_1)
b1.pack()

b2 = tk.Button(root, text='Enable', command=callback_2)
b2.pack()

root.mainloop()
