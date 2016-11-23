#!/usr/bin/env python3

# http://effbot.org/tkinterbook/canvas.htm
# http://effbot.org/tkinterbook/photoimage.htm

import tkinter as tk
from PIL import Image, ImageTk

# --- constants ---

WIDTH = 800
HEIGHT = 600

# --- functions ---

def on_click():
    w = int(c['width'])
    h = int(c['height'])
    print('minimal size:', w, h)

    w = c.winfo_width()
    h = c.winfo_height()
    print('current size:', w, h)

    c.coords(i, w//2, h//2)
    c.coords(t, w//2, h//2)
    
    w = c.winfo_reqwidth()
    h = c.winfo_reqheight()
    print('    req size:', w, h)

    # current position + (w//2, h//2)        
    #c.move(t, w//2, h//2)
    
def on_resize(event):
    # determine the ratio of old width/height to new width/height
    w = event.width
    h = event.height
    print('event size:', w, h)

    #w_scale = float(w)/width
    #h_scale = float(h)/height
    
    # resize the canvas - doesn't work with `fill` and `expand`
    #c.config(width=w, height=h)

    c.coords(i, w//2, h//2)
    c.coords(t, w//2, h//2)
    
    # rescale all the objects tagged with the "all" tag
    #self.scale("all", 0, 0, w_scale,h_scale)
    
# --- main ---

root = tk.Tk()

c = tk.Canvas(root, width=WIDTH, height=HEIGHT)
c.pack(fill='both', expand=True)
c.bind("<Configure>", on_resize)

# only GIF and PGM/PPM
#photo = tk.PhotoImage(file='test.gif')

# other formats
image = Image.open('test_transparent.png')
photo = ImageTk.PhotoImage(image)
# use in functions - solution for "garbage collector" problem
c.image = photo

# text on image
i = c.create_image((WIDTH//2, HEIGHT//2), image=photo)
t = c.create_text((WIDTH//2, HEIGHT//2), text='Hello World')

# (transparent) image on text
#t = c.create_text((WIDTH//2, HEIGHT//2), text='Hello World')
#i = c.create_image((WIDTH//2, HEIGHT//2), image=photo)

b = tk.Button(root, text='OK', command=on_click)
b.pack()

root.mainloop()
