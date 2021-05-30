import tkinter as tk
from PIL import ImageTk
from scrolledcanvas import ScrolledCanvas

# --- functions ---

# --- main ---

root = tk.Tk()              

# create scroller
s = ScrolledCanvas(root, vertical=True, horizontal=True)
s.pack(fill='both', expand=True)
s._canvas['borderwidth'] = 0
s['borderwidth'] = 0
s['relief'] = 'flat'

# ---

photo = ImageTk.PhotoImage(file='/home/furas/Obrazy/lenna.png')
label = tk.Label(s._canvas, image=photo, borderwidth=0)
s.add(label)

# ---

root.mainloop()

