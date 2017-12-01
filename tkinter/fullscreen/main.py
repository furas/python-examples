#!/usr/bin/env python3

import tkinter as tk

def on_escape(event=None):
    print("escaped")
    root.destroy()

root = tk.Tk()

#root.overrideredirect(True)  # sometimes it is needed to toggle fullscreen
                              # but then window doesn't get events from system
#root.overrideredirect(False) # 

root.attributes("-fullscreen", True) # run fullscreen
root.wm_attributes("-topmost", True) # keep on top
#root.focus_set() # set focus on window

root.bind("<Escape>", on_escape)

# close window after 5s if `ESC` will not work
root.after(5000, root.destroy) 

root.mainloop()
