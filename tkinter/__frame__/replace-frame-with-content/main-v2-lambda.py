
# date: 2019.05.04
# author: Bartłomiej 'furas' Burek

import tkinter as tk

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

# --- main frame without .pack() ---

main_frame = tk.Frame(root)

button = tk.Button(main_frame, text="Frame #1", command=lambda:change_frame(frame_1))
button.pack()

button = tk.Button(main_frame, text="Frame #2", command=lambda:change_frame(frame_2))
button.pack()

# --- frame #1 without .pack() ---

frame_1 = tk.Frame(root)

l = tk.Label(frame_1, text="It is Frame #1", bg='red')
l.pack()

b = tk.Button(frame_1, text="BACK", command=lambda:change_frame(main_frame))
b.pack()

# --- frame #2 without .pack() ---

frame_2 = tk.Frame(root)

l = tk.Label(frame_2, text="It is Frame #2", bg='green')
l.pack()

b = tk.Button(frame_2, text="BACK", command=lambda:change_frame(main_frame))
b.pack()

# --- set frame at start ---

current = main_frame
current.pack()

root.mainloop()
