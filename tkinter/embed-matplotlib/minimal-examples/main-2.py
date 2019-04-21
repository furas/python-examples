import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

data = [1, 3, 2, 4, ]

root = tkinter.Tk()

# create plot(s)
fig = plt.Figure()

fig.add_subplot('321').plot(data) # add plot (as first plot) to figure (with one row, one column)
fig.add_subplot('324').plot(data) # add plot (as first plot) to figure (with one row, one column)
fig.add_subplot('325').plot(data) # add plot (as first plot) to figure (with one row, one column)

# create canvas with plot and add (pack) to tkinter's window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

tkinter.mainloop()

