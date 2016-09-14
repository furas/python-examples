#!/usr/bin/env python3

import tkinter as tk
import tkinter.messagebox

root = tk.Tk()  # create main window
root.withdraw() # hide main window

tkinter.messagebox.showinfo("TKinter Messagebox", "Welcome to Tkinter Messagebox")

answer = tkinter.messagebox.askquestion("Question 1", "Are you a programmer?")

if answer == "yes":
    print("Welcome Programmer!")

#root.mainloop() # not needed
