# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.08
# 
# https://web.archive.org/web/20190909161413/http://effbot.org/tkinterbook/canvas.html
#

import tkinter as tk
from PIL import ImageTk, Image

# --- functions ---

def on_resize(event):
    #global photo

    canvas_w = event.width
    canvas_h = event.height

    if canvas_h > 0:
        canvas_ratio = canvas_w/canvas_h
    else:
        canvas_ratio = 0

    image_w = image.width    
    image_h = image.height

    if image_h > 0:
        image_ratio = image_w/image_h
    else:
        image_ratio = 0

    if canvas_ratio >= image_ratio:
        w = int(canvas_h * image_ratio)
        h = canvas_h
    else:
        w = canvas_w
        if image_ratio > 0:
            h = int(canvas_w / image_ratio)
        else:
            h = 0

    size = (w, h)
    
    new_image = image.resize(size)  # it keeps aspect ratio, it DOESN'T crop
    
    photo = ImageTk.PhotoImage(new_image)
    
    stage.itemconfig(img_id, image=photo)
    stage.photo = photo

    # center on canvas     
    stage.coords(img_id, canvas_w/2, canvas_h/2)
    stage.itemconfig(img_id, anchor='center')

# --- main ---

root = tk.Tk()

stage = tk.Canvas(root, width=1000, height=700)
stage.pack(fill='both', expand=True)

#root.update()  # force `mainloop()` to calculate current `width`, `height` for canvas
                # and later `stage.winfo_width()` `stage.winfo_height()` will get correct values instead `0`
    
image = Image.open('frame_vertical.jpg')  # keep original image
photo = ImageTk.PhotoImage(image)

img_id = stage.create_image(0, 0, image=photo, anchor='center')
stage.photo = photo

stage.bind('<Configure>', on_resize)  # it runs function when Canvas change size,
                                      # it runs function also at start so it doesn't need `root.update()`
root.mainloop()

