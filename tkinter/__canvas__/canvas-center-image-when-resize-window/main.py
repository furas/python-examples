# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.08
# 
# https://web.archive.org/web/20190909161413/http://effbot.org/tkinterbook/canvas.html
#

import tkinter as tk
from PIL import ImageTk, Image

# --- functions ---

def on_resize(event):
    # it respects anchor
    x = event.width/2  
    y = event.height/2
    stage.coords(img_id, x, y)  
    
    # it DOESN'T respects anchor so you have to add offset
    #x = (event.width - photo.width())/2  
    #y = (event.height - photo.height())/2
    #stage.moveto(img_id, x, y)  # doesn't respect anchor
    
# --- main ---

root = tk.Tk()

stage = tk.Canvas(root, width=1000, height=700)
stage.pack(fill='both', expand=True)

#root.update()  # force `mainloop()` to calculate current `width`, `height` for canvas
                # and later `stage.winfo_width()` `stage.winfo_height()` will get correct values instead `0`
    
image = Image.open('/home/furas/test/lenna.png')    
photo = ImageTk.PhotoImage(image)
#photo = ImageTk.PhotoImage(file='lenna.png')

size = (stage.winfo_width()/2, stage.winfo_height()/2)
img_id = stage.create_image(size, image=photo, anchor='center')
stage.photo = photo

stage.bind('<Configure>', on_resize)  # it runs function when Canvas change size,
                                      # it runs function also at start so it doesn't need `root.update()`
root.mainloop()
