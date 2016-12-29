import tkinter as tk

# --- functions ---

def select_button(widget):
    global previously_clicked

    if previously_clicked:
        previously_clicked['bg'] = widget['bg']
        previously_clicked['activebackground'] = widget['activebackground']
        previously_clicked['relief'] = widget['relief']

    widget['bg'] = 'green'
    widget['activebackground'] = 'green'
    widget['relief'] = 'sunken'

    previously_clicked = widget

# --- main ---

names = ['Button A', 'Button B', 'Button C']

root = tk.Tk()

previously_clicked = None

for name in names:
    btn = tk.Button(root, text=name)
    
    btn.config(command=lambda arg=btn:select_button(arg))
    #btn['command'] = lambda arg=btn:select_button(arg)

    btn.pack()

root.mainloop()
