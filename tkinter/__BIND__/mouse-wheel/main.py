import tkinter as tk

# --- functions ---

def mouse_wheel(event):
    global number
    
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        number -= 1
    if event.num == 4 or event.delta == 120:
        number += 1
        
    label['text'] = number

# --- main ---

number = 0

root = tk.Tk()

label = tk.Label(root, text="0")
label.pack(ipadx=15, ipady=5)

# Windows
root.bind("<MouseWheel>", mouse_wheel)
# Linux
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)

root.mainloop()
