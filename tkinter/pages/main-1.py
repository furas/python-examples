import tkinter as tk

# --- functions ---

def create_first_page(root, go_to_page):
    page = tk.Frame(root)
    
    label = tk.Label(page, text='First Page')
    label.pack()
    
    button = tk.Button(page, text='Go to Page 2', command=lambda:set_page(go_to_page))
    button.pack()
    
    return page

def create_second_page(root, go_to_page):
    page = tk.Frame(root)
    
    label = tk.Label(page, text='Second Page')
    label.pack()
    
    button = tk.Button(page, text='Go to Page 1', command=lambda:set_page(go_to_page))
    button.pack()
    
    return page

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
    'first_page': create_first_page(root, 'second_page'),
    'second_page': create_second_page(root, 'first_page'),
}
    
set_page('first_page')

root.mainloop()   
