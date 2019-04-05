
# date: 2019.04.04
# http://effbot.org/zone/tkinter-window-destroy.htm
# https://stackoverflow.com/questions/55521608/error-when-tkinter-quits-while-using-pygame/55522509#55522509

import tkinter as tk

def _delete_window():
    print("delete_window")
    try:
        global tk_open
        tk_open = False
        root.destroy()
    except:
        pass

def _destroy(event):
    global tk_open
    tk_open = False
    print("destroy")
    
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", _delete_window)
root.bind("<Destroy>", _destroy)

tk_open = True

while True:
    if tk_open:
       root.update()
