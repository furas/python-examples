import tkinter as tk

# --- classes ---
# you can put this class in separated file
# (it will need `import tkinter`)

import tkinter 

class MsgBox(tkinter.Toplevel):

    def __init__(self, title="MsgBox", message="Hello World", choice1="OK", choice2="Cancel"):
        tkinter.Toplevel.__init__(self)

        self.result = None
        
        self.choice1 = choice1
        self.choice2 = choice2

        self.title(title)
        
        self.label = tkinter.Label(self, text=message, bg='white')
        self.label.pack(ipadx=50, ipady=20)

        self.button = tkinter.Button(self, text=str(self.choice1), command=self.on_press_choice1)
        self.button.pack(side='left', ipadx=5, padx=10, pady=10)

        self.button = tkinter.Button(self, text=str(self.choice2), command=self.on_press_choice2)
        self.button.pack(side='right', ipadx=5, padx=10, pady=10)

        self.wait_window()
        
    def on_press_choice1(self):
        self.result = self.choice1
        self.destroy()
    
    def on_press_choice2(self):
        self.result = self.choice2
        self.destroy()
        
# --- functions ---

def choice_message(title, message, choice1, choice2):

    msg = MsgBox(title, message, choice1, choice2)
    # MsgBox is waiting till you close window
    return msg.result
    
def choose():
    if choice_message("Hello", "This is a message text", True, False) == True:
        print("You choose: True")
    else:
        print("You choose: False")

def about():
    msg = MsgBox()
    # MsgBox is waiting till you close window
    print("You choose:", msg.result)

# --- main ---

root = tk.Tk()

b = tk.Button(root, text="Choose", command=choose)
b.pack(fill='x', expand=True)

b = tk.Button(root, text="About", command=about)
b.pack(fill='x', expand=True)

b = tk.Button(root, text="Close", command=root.destroy)
b.pack(fill='x', expand=True)

root.mainloop()
