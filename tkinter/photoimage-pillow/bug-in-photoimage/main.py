import tkinter as tk
from PIL import ImageTk, Image

def show_image():
   
    window = tk.Toplevel()
    
    image = Image.open("image.jpg")
    w, h = image.size

    photo = ImageTk.PhotoImage(image)
    window.photo = photo # solution for bug in PhotoImage

    canvas = tk.Canvas(window, width=w, height=h)
    canvas.pack()
    
    canvas.create_image(0, 0, anchor='nw', image=photo)
    

root = tk.Tk()

b = tk.Button(root, text='IMAGE', command=show_image)
b.pack()

root.mainloop()

