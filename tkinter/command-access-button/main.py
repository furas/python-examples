
# date: 2019.04.09
# 

import tkinter as tk

# --- functions ---

def get_text(text):
    print(text)

def get_widget(widget):
    print(widget["text"])
    widget["text"] = "DONE"
    widget["bg"] = "green"
    
def get_event(event):
    print(event.widget["text"])
    event.widget["text"] = "DONE"
    event.widget["bg"] = "green"

# --- main ---

list_words = ("One", "Two", "Three")


root = tk.Tk()

# access button's text in function assigned to button
for word in list_words:
    btn = tk.Button(root, text=word, command=lambda txt=word:get_text(txt))
    btn.pack()

# access button in function assigned to button
for word in list_words:
    btn = tk.Button(root, text=word)
    btn["command"] = lambda widget=btn:get_widget(widget)
    btn.pack()

# access button in function assigned to button
for word in list_words:
    btn = tk.Button(root, text=word)
    btn.bind('<Button-1>', get_event)
    btn.pack()

root.mainloop()

