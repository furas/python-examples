import tkinter as tk
from PIL import ImageTk, Image

# --- functions ---

def on_resize(event):
    # it respects anchor
    x = event.width/2  
    y = event.height/2
    stage.coords(img_id, x, y)  
    
    # it DOESN'T respects anchor so you have to add offset
    #x = (event.width - imgtk.width())/2  
    #y = (event.height - imgtk.height())/2
    #stage.moveto(img_id, x, y)  # doesn't respect anchor

    #stage.itemconfigure(img_id, ...)
    
# --- main ---

root = tk.Tk()

stage = tk.Canvas(root, width=1000, height=700)
stage.pack(fill='both', expand=True)

#root.update()  # force `mainloop()` to calculate current `width`, `height` for canvas
                # and later `stage.winfo_width()` `stage.winfo_height()` will get correct values instead `0`
    
#imgtk = ImageTk.PhotoImage(Image.open('lenna.png'))
imgtk = ImageTk.PhotoImage(file='lenna.png')

img_id = stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
stage.image = imgtk

stage.bind('<Configure>', on_resize)  # it runs function when Canvas change size,
                                      # it runs function also at start so it doesn't need `root.update()`
root.mainloop()
