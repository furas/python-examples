try:
    import Tkinter as tk # python 2
except:
    import tkinter as tk # python 3


# --- class ---

class App(tk.Tk):
    
    def __init__(self):
        #super().__init__() # only Python 3
        tk.Tk.__init__(self) # Python 2 & 3

        # --- toolbar ---
        
        self.toolbar = tk.Frame(self)
        self.toolbar.pack()
        
        self.current_tool = tk.StringVar()
        self.current_tool.set('selector')
        
        tk.Radiobutton(self.toolbar,
            text='Selector',
            value='selector',
            variable=self.current_tool,
            indicatoron=0
        ).pack(side='left', ipadx=15, ipady=5)

        tk.Radiobutton(self.toolbar,
            text='Rectangle',
            value='rectangle',
            variable=self.current_tool,
            indicatoron=0
        ).pack(side='left', ipadx=15, ipady=5)

        tk.Radiobutton(self.toolbar,
            text='Elipse',
            value='elipse',
            variable=self.current_tool,
            indicatoron=0
        ).pack(side='left', ipadx=5, ipady=5)

        # --- canvas ---
        
        self.canvas = tk.Canvas(self)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.bind('<B1-Motion>', self.mouse_click_move)

        # ---
        
        self.current_shape = None
        self.start_position = None

        
    def change_tool(self):
        if self.current_tool.get() == 'selector':
            self.current_shape = None
        

    def mouse_click(self, event):
        for x in dir(event):
            print(x, getattr(event, x))
        
        if self.current_tool.get() == 'selector':
            pass
            #~ if self.current_shape:
                #~ self.diff = (event.x, event.y)
        elif self.current_tool.get() == 'rectangle':
            self.current_shape = self.canvas.create_rectangle(event.x, event.y, event.x+1, event.y+1, fill='red')
            self.start_position = (event.x, event.y)
            self.canvas.tag_bind(self.current_shape, '<Button-1>', lambda event, shape=self.current_shape:self.shape_click(event, shape))
        elif self.current_tool.get() == 'elipse':
            self.current_shape = self.canvas.create_oval(event.x, event.y, event.x+10, event.y+10)
            self.start_position = (event.x, event.y)

        
    def mouse_click_move(self, event):
        print('x:', event.x, 'y:', event.y)

        if self.current_shape:
            if self.current_tool.get() == 'selector':
                x1, y1, x2, y2 = self.canvas.coords(self.current_shape)
                self.canvas.coords(self.current_shape,
                    event.x + self.diff[0], event.y + self.diff[1],
                    event.x + self.diff[2], event.y + self.diff[3])
            else:
                self.canvas.coords(self.current_shape, self.start_position[0], self.start_position[1], event.x, event.y)


    def shape_click(self, event, object_id):
        print('event:', event)
        print('object_id:', object_id)
        
        if self.current_tool.get() == 'selector':
            # unselect previouse shape
            if self.current_shape:
                self.canvas.itemconfig(self.current_shape, dash=[])
                
            # select new shape
            self.current_shape = object_id
            self.canvas.itemconfig(object_id, dash=[3,3])
            
            x1, y1, x2, y2 = self.canvas.coords(self.current_shape)
            self.diff = (x1 - event.x, y1 - event.y, x2 - event.x, y2 - event.y)
        
    def run(self):
        self.mainloop()
        
#~ class MyCanvas(tk.Canvas):
    #~ '''
    #~ Inherits Canvas class (all Canvas methodes, attributes will be accessible)
    #~ You can add your customized methods here.
    #~ '''
    #~ 
    #~ def __init__(self,master,*args,**kwargs):
        #~ tk.Canvas.__init__(self, master=master, *args, **kwargs)
        #~ self.poly = None
#~ 
    #~ def create_poly(self, points, outline='gray', fill='gray', width=2):
        #~ self.poly = self.create_polygon(points, outline=outline, fill=fill, width=width)
                    #~ 
    #~ def set_poly_fill(self, color):
        #~ if self.poly:
            #~ self.itemconfig(self.poly, fill=color)

# --- main ---
    
App().run()
