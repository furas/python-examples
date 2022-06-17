# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.17
# [python - boggle game with combination of pygame and tkinter - Stack Overflow](https://stackoverflow.com/questions/72660152/boggle-game-with-combination-of-pygame-and-tkinter)

# [8.7. Canvas arc objects](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_arc.html)

import tkinter as tk

# --- functions ---

def update_clock():
    global extent

    # negative value = reverse direction
    extent -= 3

    # red PIESLICE
    canvas.itemconfig(clock1_id, extent=extent)

    # blue ARC
    canvas.itemconfig(clock2_id, extent=extent)

    # repeate after 50ms (0.05s)
    root.after(50, update_clock)

# --- main ---

extent = 0

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# red PIESLICE
clock1_id = canvas.create_arc(150-50, 150-50, 150+50, 150+50, start=0, extent=0, outline='red', fill='red')

# blue ARC (on top of red PIESLICE)
clock2_id = canvas.create_arc(150-50, 150-50, 150+50, 150+50, style='arc', start=0, extent=0, width=5, outline='blue')


update_clock()

root.mainloop()
