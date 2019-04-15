
# date: 2019.04.15
# http://seaborn.pydata.org/examples/many_pairwise_correlations.html

# seaborn in matplotlib - tkinter doesn't need it
#import matplotlib
#matplotlib.use('TkAgg')

# embed matplotlib in tkinter 
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

# seaborn example
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import numpy as np

# --- functions ----

# Seaborn plot

def create_plot():
    sns.set(style="white")
    
    # Generate a large random dataset
    rs = np.random.RandomState(33)
    d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                     columns=list(ascii_letters[26:]))
    
    # Compute the correlation matrix
    corr = d.corr()
    
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))
    
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    return f

def on_key_press(event):
	# add own function
    print("you pressed {}".format(event.key))
    # run original handler with shortcuts (S - save in file)
    key_press_handler(event, canvas, toolbar)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

# function assigned to button with left arrow in NavigationToolbar
def my_function():
	print("Left Arrow")
    
# --- main ---

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

label = tkinter.Label(root, text="Matplotlib with Seaborn in Tkinter")
label.pack()

# --- seaborn's plot

fig = create_plot()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
#canvas.draw() # ???
#canvas.get_tk_widget().pack()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) # it will resize plot

# --- catch keys pressed on canvas (?or in all window?) to run own function or shortcuts (S - save in file)

canvas.mpl_connect("key_press_event", on_key_press)

# --- add navigation toolbar to canvas

toolbar = NavigationToolbar2Tk(canvas, root) # it has to be `canvas` with figure to have access to `figure`
#toolbar.update() # ???

# --- add button to NavigationToolbar2Tk

button = tkinter.Button(master=toolbar, text="Quit", command=_quit)
#button.pack()
button.pack(side="left")

# -- assing own function to button with left arrow

toolbar.children['!button2'].config(command=my_function)
#for item in toolbar.children: print(item) # print(item.config())

# ---

tkinter.mainloop()

