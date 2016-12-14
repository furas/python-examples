#!/usr/bin/env python3

import tkinter as tk

# --- constants ---

FONT_SIZE = 14  # Change this to change all font sizes in the program

# --- classes ---

class MyButton(tk.Label):
    
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)

        # mouse hover
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.config(
            anchor=tk.CENTER,
            background="black",
            foreground="white",
            font=("default", FONT_SIZE),
        )

    def on_enter(self, event):
        self.config(background="gray")

    def on_leave(self, event):
        self.config(background="black")

# --- functions ---

def command_exit():
    print("exit")
    root.destroy()

# --- main ---

root = tk.Tk()

root.geometry("800x600")
root.config(background="#444")

# MyButton

new_game_button = MyButton(root, text="New Game", width=10)
new_game_button.pack(ipadx=10, ipady=10)

load_game_button = MyButton(root, text="Load Game", width=10)
load_game_button.pack(ipadx=10, ipady=10)

options_button = MyButton(root, text="Options", width=10)
options_button.pack(ipadx=10, ipady=10)

# Exit Button

exit_button = tk.Button(root, text="Exit", width=10)
exit_button.pack(ipadx=0, ipady=7)

exit_button.config(
    anchor=tk.CENTER,
    font=("default", FONT_SIZE),

    # without border
    borderwidth=0,
    highlightthickness=0,

    # Leave colors
    background="black",
    foreground="white",

    # Enter colors
    activebackground="grey",
    activeforeground="white",

    # run on click
    command=command_exit
)

root.mainloop()
