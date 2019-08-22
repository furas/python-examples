import tkinter as tk

# --- classes ---

class FirstPage(tk.Frame):
        
    def __init__(self, master, go_to_page, *args):
        super().__init__(master, *args)

        self.go_to_page = go_to_page
        
        self.label = tk.Label(self, text='First Page')
        self.label.pack()
    
        self.button = tk.Button(self, text='Go to Page 2', command=lambda:set_page(go_to_page))
        self.button.pack()

class SecondPage(tk.Frame):
        
    def __init__(self, master, go_to_page, *args):
        super().__init__(master, *args)

        self.go_to_page = go_to_page
        
        self.label = tk.Label(self, text='Second Page')
        self.label.pack()
    
        self.button = tk.Button(self, text='Go to Page 2', command=lambda:set_page(go_to_page))
        self.button.pack()

# --- functions ---

def set_page(page):
    global current_page
    
    if current_page is not None:
        current_page.pack_forget()
        
    current_page = all_pages[page]
    current_page.pack()
    
# --- main ---

root = tk.Tk()

current_page = None

all_pages = {
    'first_page':  FirstPage(root, 'second_page'),
    'second_page': SecondPage(root, 'first_page'),
}
    
set_page('first_page')

root.mainloop()   
