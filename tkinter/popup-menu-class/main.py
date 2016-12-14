#!/usr/bin/env python3

import tkinter as tk

# --- classes ---

class NodePopup(tk.Menu):
    
    def __init__(self, master):
        super().__init__(master, tearoff=0)
        
        self.send_disabled = tk.BooleanVar()
        
        self.add_checkbutton(label="Disable sending", 
            variable=self.send_disabled, command=self.toggle_send)

    def popup(self, event):
        #self.send_disabled.set(0)
        print('send_disabled:', self.send_disabled.get())
        self.post(event.x_root, event.y_root)
        
    def toggle_send(self):
        print('send_disabled:', self.send_disabled.get())

# --- functions ---

def change():
    state = not menu.send_disabled.get()
    menu.send_disabled.set(state)

# --- main ---

root = tk.Tk()
root.pack_propagate(0)

menu = NodePopup(root)
root.bind('<Button-3>', menu.popup)

b = tk.Button(root, text='Change', command=change)
b.pack()

root.mainloop()
