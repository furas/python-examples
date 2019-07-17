
# date: 2019.07.14
# https://stackoverflow.com/questions/57025748/tkinter-label-text-not-updating-label-is-visible-and-text-value-is-up-to-date

import tkinter as tk

def add_char():
    global label_index
    global running

    # add next char to label
    label['text'] += text[label_index]
    label_index += 1

    # check if there is need to run it again
    if label_index < len(text):
        # run again after 200ms
        root.after(200, add_char)
    else:
        # unblock button
        running = False
        
def start():
    global label_index
    global running

    # check if animation is running
    if not running:
        # block button
        running = True
        
        # reset settings
        label['text'] = ''
        label_index = 0
        
        # run animation
        add_char()
    
# ---

text = 'Hello World'
label_index = 0
running = False

root = tk.Tk()

label = tk.Label(root)
label.pack()

button = tk.Button(root, text="Start", command=start)
button.pack()

root.mainloop()
