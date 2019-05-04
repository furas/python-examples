
# date: 2019.05.04
# author: Bartłomiej 'furas' Burek

import tkinter as tk

# --- classes ---

class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        button = tk.Button(self, text="Frame #1", command=lambda:change_frame(frame_1))
        button.pack()

        button = tk.Button(self, text="Frame #2", command=lambda:change_frame(frame_2))
        button.pack()


class Frame1(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        l = tk.Label(self, text="It is Frame #1", bg='red')
        l.pack()

        b = tk.Button(self, text="BACK", command=lambda:change_frame(main_frame))
        b.pack()


class Frame2(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        l = tk.Label(self, text="It is Frame #2", bg='green')
        l.pack()

        b = tk.Button(self, text="BACK", command=lambda:change_frame(main_frame))
        b.pack()

# --- functions ---

def change_frame(new_frame):
    global current

    # hide current tk.Frame
    current.pack_forget()

    # show new tk.Frame
    current = new_frame
    current.pack()

# --- main ---

root = tk.Tk()

# --- pages without .pack() before Main Page---

frame_1 = Frame1(root)
frame_2 = Frame2(root)

# --- main frame without .pack() ---

main_frame = MainFrame(root)

# ---

current = main_frame
current.pack()

root.mainloop()
