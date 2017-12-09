#!/usr/bin/env python3

import tkinter as tk
from scrolledframe import ScrolledFrame
from random import randint

class Question:

    def __init__(self, parent, question, answer):
        self.parent = parent
        self.question = question
        self.answer = answer
        self.create_widgets()

    def get_input(self):
        if self.answer == self.entry.get():
            self.label['text'] = "Good: {} = {}".format(self.question, self.answer)
            self.entry['state'] = 'disable'
            self.button['state'] = 'disable'

    def create_widgets(self):
        self.labelframe = tk.LabelFrame(self.parent, text="Question:")
        self.labelframe.pack(fill="both", expand=True)

        self.label = tk.Label(self.labelframe, text=self.question + ' ?')
        self.label.pack(expand=True, fill='both')

        self.entry = tk.Entry(self.labelframe)
        self.entry.pack()

        self.button = tk.Button(self.labelframe, text="Click", command=self.get_input)
        self.button.pack()

# --- main ---

root = tk.Tk()
root.title("Quiz")
root.geometry("400x300")

window = ScrolledFrame(root)
window.resize_width = True # resize inner frame to canvas size
window.pack(expand=True, fill='both')

for i in range(10):
    x = randint(1, 20)
    y = randint(1, 20)
    Question(window.inner, "{} + {}".format(x, y), str(x + y))

root.mainloop()
