import tkinter as tk

# --- functions ---

def select_button():
    print('value:', v.get())
    
# --- main ---

names = ['Button A', 'Button B', 'Button C']

root = tk.Tk()

v = tk.IntVar()

for i, name in enumerate(names, 2):
    btn = tk.Radiobutton(root, text=name, variable=v, value=i)
    
    btn['indicatoron'] = 0
    btn['selectcolor']='green'
    
    btn['command'] = select_button

    btn.grid(row=i, column=0, sticky='w', ipadx=5, ipady=5)

root.mainloop()
