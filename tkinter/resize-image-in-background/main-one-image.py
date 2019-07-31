import tkinter as tk
from PIL import Image, ImageTk

def on_resize(event):
    global photo # solution for bug in PhotoImage

    #print('[DEBUG] on_resize:', event.widget)

    # resize only when root change size
    if str(event.widget) == '.':
        # calculate new size of image
        width  = event.width   # - 2 # 2*border
        height = event.height  # - 2 # 2*border
        
        # generate new image
        rescaled_img = original_img.resize((width, height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(rescaled_img)

        # replace images in labels
        label['image'] = photo
        #event.widget['image'] = photo

# ---- main ---

# load image and rescale it at start
original_img = Image.open('image.png')

root = tk.Tk()

photo = ImageTk.PhotoImage(original_img)

label = tk.Label(root, image=photo, border=0) # if border > 0 then you have to use `-2*border` in on_resize
label.pack(fill='both', expand=True)

root.bind('<Configure>', on_resize)

root.mainloop()
