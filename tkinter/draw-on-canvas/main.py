try:
    import Tkinter as tk # python 2
except:
    import tkinter as tk # python 3


# --- class ---

class App(tk.Tk):
    
    def __init__(self):
        #super().__init__() # only Python 3
        tk.Tk.__init__(self) # Python 2 & 3

        self.toolbar = tk.Frame(self)
        self.toolbar.pack()
        
        self.current_tool = tk.StringVar()
        self.current_tool.set('selector')
        
        self.tool_button = {}
        
        self.tool_button['selector'] = tk.Radiobutton(self.toolbar, text='Selector', value='selector', variable=self.current_tool, indicatoron=0)
        self.tool_button['selector'].pack(side='left', ipadx=15, ipady=5)

        self.tool_button['rectangle'] = tk.Radiobutton(self.toolbar, text='Rectangle', value='rectangle', variable=self.current_tool, indicatoron=0)
        self.tool_button['rectangle'].pack(side='left', ipadx=15, ipady=5)

        self.tool_button['elipse'] = tk.Radiobutton(self.toolbar, text='Elipse', value='elipse', variable=self.current_tool, indicatoron=0)
        self.tool_button['elipse'].pack(side='left', ipadx=5, ipady=5)

        self.canvas = tk.Canvas(self)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.bind('<B1-Motion>', self.mouse_click_move)

        self.current_shape = None
        
    def mouse_click(self, event):
        #print('click', '\n'.join(dir(event)))
        print('x:', event.x, 'y:', event.y)
        
        if self.current_tool.get() == 'selector':
            self.current_shape = None
            #TODO: find nearest object
        elif self.current_tool.get() == 'rectangle':
            self.current_shape = self.canvas.create_rectangle(event.x, event.y, event.x+1, event.y+1)
        elif self.current_tool.get() == 'elipse':
            self.current_shape = self.canvas.create_oval(event.x, event.y, event.x+10, event.y+10)
        
    def mouse_click_move(self, event):
        print('x:', event.x, 'y:', event.y)

        if self.current_shape:
            x1, y1, x2, y2 = self.canvas.coords(self.current_shape)
            self.canvas.coords(self.current_shape, x1, y1, event.x, event.y)
            
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
