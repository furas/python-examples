
# date: 2019.07.24
# may not works on Windows Home 64-bit

import tkinter as tk
import tkinter.messagebox as messagebox


# blocking without message 
def on_closing_x():
    pass

def on_closing():
#    if messagebox.askokcancel("Quit", "Do you want to quit?"):
#        root.destroy()
    pass

root = tk.Tk()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
