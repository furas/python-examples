import tkinter as tk


def hello():
    print("hello!")

def popup(event):
    menu.post(event.x_root, event.y_root)
    menu.focus()
    
def popup_close(event):
    menu.unpost()


root = tk.Tk()

# frame
frame = tk.Frame(root, width=512, height=512)
frame.pack()

# popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)

# events
frame.bind("<Button-3>", popup)
frame.bind("<Button-1>", popup_close)
menu.bind("<Escape>", popup_close)

root.mainloop()
