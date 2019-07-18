
# date: 2019.07.18

import tkinter as tk
from PIL import Image, ImageTk

class AnimatedLabel(tk.Label):
    
    def __init__(self, *args, images=None, delay=100, state='Idle', **kwargs):
        super().__init__(*args, **kwargs)
        
        self.images = images
        self.delay = delay
        self.state = state
        self.current_frame = 0
        
    def start(self):        
        self.next_frame()
        
    def next_frame(self):
        if self.state == 'Idle':
            # change image
            self.frame = self.images[self.current_frame]
            self.configure(image=self.frame)
            
            # get next frame (or first frame)
            self.current_frame = (self.current_frame+1) % len(self.images)
        
        # run again after 'delay' milliseconds
        self.after(self.delay, self.next_frame)
    
class Application():
    
    def __init__(self):

        # WINDOW SETUP
        self.root = tk.Tk()
        self.root.geometry('512x512')
        self.root.protocol('WM_DELETE_WINDOW', self.annihilation)

        self.load_images()
        
        # CALL THE ANIMATION FUNCTION
        self.animation1 = AnimatedLabel(self.root, images=self.images, delay=500)
        self.animation1.place(relx=.5, rely=.5, anchor="c")


        self.animation2 = AnimatedLabel(self.root, images=self.images, delay=125)
        self.animation2.place(relx=.1, rely=.1, anchor="c")
        
        self.animation1.start()
        self.animation2.start()

        self.root.mainloop()


    # LIST OF IMAGES
    def load_images(self):
        self.filenames = [
            'Obrazy/21586784_1642005829205281_8345912444787042013_o.jpg',
            'Obrazy/37884728_1975437959135477_1313839270464585728_n.jpg'            
            #'Image1.tif',
            #'Image2.tif',
        ]
        self.images = []
        for filename in self.filenames:
            img = ImageTk.PhotoImage(Image.open(filename).resize((512, 512)))
            self.images.append(img)
    
    def annihilation(self):
        #self.root.eval('::ttk::CancelRepeat')
        self.state = 'Quitting'
        self.root.destroy()

Application()
