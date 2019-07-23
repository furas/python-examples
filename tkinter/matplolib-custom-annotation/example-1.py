
# date: 2019.07.19

import tkinter as tk                                                    
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- data ---

mapArr = (
    [113, 62, 31, 63],
    [50, 101, 72, 47],
    [92, 10, 40, 12],
    [83, 21, 128, 16]
)

xy = ('A','B','C','D','E','F')

# --- functions ---

def on_mouse_move(event):
    if checkbuttonvariable.get() == 0:
        return
    
    if event.inaxes == axis:
        annotation.xy = (event.xdata, event.ydata)

        row = int(round(event.ydata))
        col = int(round(event.xdata))
        value = mapArr[row][col]

        annotation.set_text(str(value))

        annotation.set_visible(True)
    else:
        annotation.set_visible(False)
        
    canvas.draw_idle()
    #canvas.draw()
                            
# --- main ---

root = tk.Tk()                                                          

figure = matplotlib.figure.Figure()
axis = figure.add_subplot()

# add plot to tkinter window
canvas = FigureCanvasTkAgg(figure, root)                                
canvas.get_tk_widget().pack(fill='both', expand=True)

heatmap = axis.imshow(mapArr, cmap="gray", interpolation='nearest', vmin=0, vmax=128)        
heatmap.axes.get_xaxis().set_visible(False)                             
heatmap.axes.get_yaxis().set_visible(False)

colorbar = figure.colorbar(heatmap)

# ---

# need "offset point" to display near mouse cursor
annotation = axis.annotate("",
                    xy=(0,0), xytext=(20,20), textcoords="offset points",
                    arrowprops=dict(arrowstyle="->"), visible=False,
                    bbox=dict(boxstyle="round", fc="w"))

canvas.mpl_connect('motion_notify_event', on_mouse_move)

# ---

# control annotation
checkbuttonvariable = tk.IntVar(value=1)
button = tk.Checkbutton(root, text='Visible', variable=checkbuttonvariable)
button.pack()

#---

root.mainloop()
