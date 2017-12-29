import tkinter as tk

# 
# https://stackoverflow.com/a/19842646/1832058
# Nov 7 '13 at 17:29
#
# changes: 2017.12.29
#

# --- classes ---

class MainWindow():

    def __init__(self, master):

        # canvas for image
        self.canvas = tk.Canvas(master, width=60, height=60)
        self.canvas.pack()

        # images
        self.all_images = [
            tk.PhotoImage(file='ball1.gif'),
            tk.PhotoImage(file='ball2.gif'),
            tk.PhotoImage(file='ball3.gif')
        ]

        # set first image on canvas
        self.image_index = 0
        
        self.selected_image = self.all_images[self.image_index]
        
        self.object_id = self.canvas.create_image(0, 0, anchor='nw', image=self.selected_image)

        # button to change image
        self.button = tk.Button(master, text='Change', command=self.on_button)
        self.button.pack()

    def on_button(self):

        # next image module "number of images" so it will loop
        self.image_index = (self.image_index + 1) % len(self.all_images)
        
        self.selected_image = self.all_images[self.image_index]
        
        self.canvas.itemconfig(self.object_id, image=self.selected_image)

# --- main ---

root = tk.Tk()
MainWindow(root)
root.mainloop()
