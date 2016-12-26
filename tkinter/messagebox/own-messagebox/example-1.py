import tkinter as tk


# --- functions ---

def about():

    win = tk.Toplevel()
    win.title("ABOUT")
    
    l = tk.Label(win, text="One\nTwo Two\nThree Three Three", bg='white')
    l.pack(ipadx=50, ipady=10, fill='both', expand=True)
    
    b = tk.Button(win, text="OK", command=win.destroy)
    b.pack(pady=10, padx=10, ipadx=20, side='right')
    
# --- main ---

root = tk.Tk()

b = tk.Button(root, text="About", command=about)
b.pack(fill='x', expand=True)

b = tk.Button(root, text="Close", command=root.destroy)
b.pack(fill='x', expand=True)

root.mainloop()
