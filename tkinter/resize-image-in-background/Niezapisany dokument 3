import tkinter as tk
from PIL import Image, ImageTk

def on_resize(event):
    global rescaled_img
    global photo

    #print('[DEBUG] on_resize:', event.widget)

    # resize only when root change size
    if str(event.widget) == '.':
        # generate new image
        width  = event.width//2# - 2 # 2*border
        height = event.height  # - 2 # 2*border
        rescaled_img = original_img.resize((width, height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(rescaled_img)

        # replace images in labels
        #label_left['image'] = photo
        #label_right['image'] = photo
        event.widget['image'] = photo

# ---- main ---

original_img = Image.open('image.jpg')
rescale = 0.4
width = int(rescale * original_img.width)
height = int(rescale * original_img.height)
rescaled_img = original_img.resize((width, height), Image.ANTIALIAS)

root = tk.Tk()

photo = ImageTk.PhotoImage(rescaled_img)

label_left = tk.Label(root, image=photo, border=0) # if border > 0 then you have to use `-2*border` in on_resize
label_left.pack(side='left', fill='both', expand=True)

label_right = tk.Label(root, image=photo, border=0) # if border > 0 then you have to use `-2*border` in on_resize
label_right.pack(side='left', fill='both', expand=True)

root.bind('<Configure>', on_resize)

root.mainloop()
