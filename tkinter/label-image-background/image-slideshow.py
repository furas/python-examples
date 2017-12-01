import tkinter as tk
from PIL import ImageTk

# --- function ---

def change_image():
    global current_image

    current_image = (current_image+1) % len(images)    
    image_label['image'] = images[current_image]
    
    root.after(1000, change_image)

# --- main ---

names = [
    'Obrazy/gory, tatry, bieszczady/15025155_1323028051043141_4635999762716208068_o.jpg',
    'Obrazy/gory, tatry, bieszczady/15129586_1332634746749138_3927511402371119417_o.jpg',
    'Obrazy/gory, tatry, bieszczady/15138384_1332634740082472_8926296375886772446_o.jpg',
    'Obrazy/gory, tatry, bieszczady/15195818_1334808379865108_2983569449704230739_o.jpg',
]
images = []
current_image = 0
    
root = tk.Tk()
root.geometry("800x600")

for name in names:
    img = ImageTk.PhotoImage(file=name)
    images.append(img)
    
image_label = tk.Label(root)
image_label.pack()

change_image()

root.mainloop()
