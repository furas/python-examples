import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyClass():

    def __init__(self):

        self.sheets = [[1,2,3], [3,1,2], [1,5,1]]
        self.W = 2
        self.L = 5
        self.all_figures = []

    def plot_sheet(self, data):
        """plot single figure"""

        fig, ax = plt.subplots(1)

        ax.set_xlim([0, self.W]) 
        ax.set_ylim([0, self.L])

        ax.plot(data)

        return fig

    def generate_all_figures(self):
        """create all figures and keep them on list"""

        for data in self.sheets:
            fig = self.plot_sheet(data)
            self.all_figures.append(fig)

def show_figure(number):
    global dataPlot

    # remove old canvas
    if dataPlot is not None: # at start there is no canvas to destroy
        dataPlot.get_tk_widget().destroy()

    # get figure from list
    one_figure = my_class.all_figures[number]

    # display canvas with figuere
    dataPlot = FigureCanvasTkAgg(one_figure, master=window)
    dataPlot.draw()
    dataPlot.get_tk_widget().grid(row=0, column=0)

def on_prev():
    global selected_figure

    # get number of previous figure
    selected_figure -= 1
    if selected_figure < 0:
        selected_figure = len(my_class.all_figures)-1

    show_figure(selected_figure)

def on_next():
    global selected_figure

    # get number of next figure
    selected_figure += 1
    if selected_figure > len(my_class.all_figures)-1:
        selected_figure = 0

    show_figure(selected_figure)

# --- main ---

my_class = MyClass()
my_class.generate_all_figures()

window = tk.Tk()
window.rowconfigure(0, minsize=500)    # minimal height
window.columnconfigure(0, minsize=700) # minimal width

# display first figure    
selected_figure = 0
dataPlot = None # default value for `show_figure`
show_figure(selected_figure)

# add buttons to change figures
frame = tk.Frame(window)
frame.grid(row=1, column=0)

b1 = tk.Button(frame, text="<<", command=on_prev)
b1.grid(row=0, column=0)

b2 = tk.Button(frame, text=">>", command=on_next)
b2.grid(row=0, column=1)

window.mainloop()
