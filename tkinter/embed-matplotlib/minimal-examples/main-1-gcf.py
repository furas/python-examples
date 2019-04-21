import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

data = [1, 3, 2, 4]

root = tkinter.Tk()

# create plot
plt.plot(data)
fig = plt.gcf() # get current figure

# create canvas with plot and add (pack) to tkinter's window
canvas = FigureCanvasTkAgg(fig, master=root) # fig = figure with plot, master = window, frame or widget which has to display it
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1) # `side='top', fill='both', expand=1` will resize plot when you resize window

tkinter.mainloop()
