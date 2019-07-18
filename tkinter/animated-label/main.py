
# date: 2019.07.18

import tkinter as tk
from PIL import Image, ImageTk



class AnimatedLabel(tk.Label):
    
    def __init__(self, *args, images=None, delay=100, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.images = images
        self.delay = delay

        self.current_frame = 0
        self.running = False
    
        self.job_id = None
            
    def start(self):     
        if not self.running:
            self.running = True   
            self.next_frame()
        else:
            print("already running")
        
    def stop(self):
        if self.running:
            self.running = False
            if self.job_id:
                self.after_cancel(self.job_id)
        else:
            print("not running")
            
    def next_frame(self):
    
        if self.running:
            # change image
            self.frame = self.images[self.current_frame]
            self.configure(image=self.frame)
            
            # get next frame (or first frame)
            self.current_frame = (self.current_frame+1) % len(self.images)
        
            # run again after 'delay' milliseconds
            self.job_id = self.after(self.delay, self.next_frame)
    
    
class Application(tk.Tk):
    
    def __init__(self, width=500, height=500):
        super().__init__()
        
        #self.geometry('{}x{}'.format(width, height))
        self.protocol('WM_DELETE_WINDOW', self.on_exit)

        # images for both animations
        self.load_images()
        
        # create two aniamted labels with different speed/delay
        
        self.animation1 = AnimatedLabel(self, images=self.images, delay=500)
        self.animation1.pack(side='left')

        self.animation2 = AnimatedLabel(self, images=self.images, delay=250)
        self.animation2.pack(side='left')
        
        self.animation3 = AnimatedLabel(self, images=self.images, delay=125)
        self.animation3.pack(side='left')

        # start both at the same moment
        
        self.animation1.start()
        self.animation2.start()
        self.animation3.start()

    def run(self):
        self.mainloop()

    def load_images(self, size=None):
        self.filenames = [
            'ball1.png', 
            'ball2.png', 
            'ball3.png',
        ]
        self.images = []
        for filename in self.filenames:
            img = Image.open(filename)
            if size:
                img = img.resize((size, size))
            img = ImageTk.PhotoImage(img)
            self.images.append(img)
    
    def on_exit(self):
        #self.eval('::ttk::CancelRepeat')
        self.destroy()

if __name__ == '__main__':
    app = Application()
    app.run()
