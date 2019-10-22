import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# --- functions ---

def eggs():
    print("eggs")

# --- main ---

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
AS = [10/2**0]

# ---

root = tk.Tk()
root.geometry("600x600")
root.title("eggs")

# ---

frame_top = tk.Frame(root)
frame_top.pack(fill='both', expand=True)

fig = Figure(dpi=100)#, figsize=(10, 6))
fig.add_subplot(111).plot(x,y)
#fig.add_subplot(111).plot(AS)

canvas = FigureCanvasTkAgg(fig, master=frame_top)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(fill='both', expand=True)

toolbar = NavigationToolbar2Tk(canvas, frame_top)
toolbar.update()

tool = tk.Button(toolbar, text="my tool")
tool.pack(side='left')#, fill='x', expand=True)

# ---

frame_bottom = tk.Frame(root)
frame_bottom.pack(fill='x')

button1 = tk.Button(frame_bottom, text="button1")
button1.pack(side='left', fill='x', expand=True)

button2 = tk.Button(frame_bottom, text="button2")
button2.pack(side='left', fill='x', expand=True)

button3 = tk.Button(frame_bottom, text="button3")
button3.pack(side='left', fill='x', expand=True)

# ---

root.mainloop()

