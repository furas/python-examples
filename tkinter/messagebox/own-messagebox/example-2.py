import tkinter as tk

# --- classes ---
# you can put this in separated file (it will need `import tkinter`)

import tkinter 

class MsgBox(tkinter.Toplevel):

    def __init__(self, title="MsgBox", message="Hello World"):
        tkinter.Toplevel.__init__(self)

        self.title(title)
        
        self.label = tkinter.Label(self, text=message)
        self.label['bg'] = 'white'
        self.label.pack(ipadx=50, ipady=10, fill='both', expand=True)

        self.button = tkinter.Button(self, text="OK")
        self.button['command'] = self.destroy
        self.button.pack(pady=10, padx=10, ipadx=20, side='right')
        
# --- functions ---

def about():

    msg = MsgBox("ABOUT", "One\nTwo Two\nThree Three Three")
    msg.label['font'] = 'Verdana 20 bold'
    msg.button['text'] = 'Close'
    msg.button.pack(side='left')
    
# --- main ---

root = tk.Tk()

b = tk.Button(root, text="About", command=about)
b.pack(fill='x', expand=True)

b = tk.Button(root, text="Close", command=root.destroy)
b.pack(fill='x', expand=True)

root.mainloop()
