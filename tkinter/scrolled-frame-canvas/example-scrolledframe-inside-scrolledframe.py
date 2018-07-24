import tkinter as tk
from PIL import Image, ImageTk


class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0, sticky='news') # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = tk.Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = tk.Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky='we')
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = tk.Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=1) # changed
        self.rowconfigure(0, weight=1) # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)
        
        # resize inner frame to canvas size
        self.resize_width = False
        self.resize_height = False
        self._canvas.bind('<Configure>', self.inner_resize)

    def resize(self, event=None): 
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

    def inner_resize(self, event):
        # resize inner frame to canvas size
        if self.resize_width:
            self._canvas.itemconfig(self._window, width=event.width)
        if self.resize_height:
            self._canvas.itemconfig(self._window, height=event.height)


# --- main ---

root = tk.Tk()              

# ---

canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky='news')

root.columnconfigure(0, weight=1) # changed
root.rowconfigure(0, weight=1) # changed

sf = ScrolledFrame(root, vertical=False) # turn off scrollbar inside ScrolledFrame
window = canvas.create_window((100, 0), window=sf, anchor='nw', width=150)#, height=100)

#sf.resize_height = True  # <-- added
sf.resize_width = True  # <-- added

# assign external scrollbar to ScrolledFrame
vertical_bar = tk.Scrollbar(root, orient='vertical', command=sf._canvas.yview)
vertical_bar.grid(row=0, column=1, sticky='ns')
sf._canvas.configure(yscrollcommand=vertical_bar.set)

sf2 = ScrolledFrame(sf.inner)  # <-- added
sf2.pack()  # <-- added

tk.Button(sf.inner, text="BUTTON").pack()

sf3 = ScrolledFrame(sf.inner)  # <-- added
sf3.pack()  # <-- added

canvas.create_rectangle((0, 0, 300, 200), fill='red')
canvas.create_rectangle((50, 100, 400, 400), fill='green')

# ---

# add some items to scrolled frame

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
variables = []

# add widgets to scrolled frame - as parent you have to use `sf.inner` instead of `sf`
for txt in data:
    var = tk.IntVar()
    variables.append(var)
    l = tk.Checkbutton(sf2.inner, text=txt, variable=var)  # <-- added sf2 instead of sf
    l.grid(sticky='w')

# ---

root.mainloop()
