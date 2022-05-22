# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.05.22

# 
# detect click on circle button and change image
#

import tkinter as tk
        
# --- functions ---

def on_click(event):
    global selected 
    
    #print('event:', event)
    #print('x:', event.x)
    #print('y:', event.y)
    
    x1, y1, x2, y2 = canvas.bbox(button_id)
    #print('bbox [x1, y1, x2, y2]:', x1, y1, x2, y2)
    
    #if (x1 <= event.x <= x2) and (y1 <= event.y <= y2):
    #    print('clicked rectangle [x1, x2, y2, y2]:', [x1, x2, y2, y2])

    center_x = (x2+x1)//2
    center_y = (y2+y1)//2
    r = (x2-x1)//2
    
    temp_x = event.x - center_x
    temp_y = event.y - center_y
    
    if temp_x**2 + temp_y**2 <= r**2:
        print('clicked circle [cx, cy, r]:', [center_x, center_y, r])
        if not selected:
            selected = True
            canvas.itemconfig(button_id, image=button_img_rgb)
        else:
            selected = False
            canvas.itemconfig(button_id, image=button_img_gray)
                
# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=512, height=512)
canvas.pack()
canvas.bind('<Button-1>', on_click)

background = tk.PhotoImage(file='images/lenna.png')
background_id = canvas.create_image((0, 0), image=background, anchor='nw')

# ---

selected = False  # to change image
button_img_gray = tk.PhotoImage(file='images/hal9000-gray.png')
button_img_rgb  = tk.PhotoImage(file='images/hal9000.png')
button_id = canvas.create_image((256, 125), image=button_img_gray, anchor='center')

# ---

root.mainloop()   
