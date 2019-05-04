import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext

def send_data():
    txt.insert('end', combo.get() + '\n')

root = tk.Tk()

label = tk.Label(root, text="Location:")
label.pack()

combo = ttk.Combobox(root, values=("Chicago","NY", "Texas"))
combo.pack()
combo.current(0)

button = tk.Button(root, text="Send", command=send_data)
button.pack()

txt = scrolledtext.ScrolledText(root)
txt.pack()

root.mainloop()
