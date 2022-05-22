# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.08
# 
# https://web.archive.org/web/20190909161413/http://effbot.org/tkinterbook/canvas.html
#
# [python - How to center an image in tkinter with PIL - Stack Overflow](https://stackoverflow.com/questions/72160551/how-to-center-an-image-in-tkinter-with-pil/)

import tkinter as tk
from PIL import ImageTk, Image, ImageOps

# --- functions ---

def on_resize(event):
    #global photo
    
    size = (event.width, event.height)

    new_image = ImageOps.fit(image, size)  # it keeps aspect ratio, but it crops
    
    photo = ImageTk.PhotoImage(new_image)

    stage.itemconfig(img_id, image=photo)
    stage.photo = photo

# --- main ---

root = tk.Tk()

stage = tk.Canvas(root, width=1000, height=700)
stage.pack(fill='both', expand=True)

#root.update()  # force `mainloop()` to calculate current `width`, `height` for canvas
                # and later `stage.winfo_width()` `stage.winfo_height()` will get correct values instead `0`
    
image = Image.open('frame_vertical.jpg')  # keep original image
photo = ImageTk.PhotoImage(image)

img_id = stage.create_image(0, 0, image=photo, anchor='nw')
stage.photo = photo

stage.bind('<Configure>', on_resize)  # it runs function when Canvas change size,
                                      # it runs function also at start so it doesn't need `root.update()`
root.mainloop()
