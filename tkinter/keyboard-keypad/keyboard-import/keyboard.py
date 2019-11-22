import tkinter as tk

alphabets = [
    ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']',"\\"],
    ['Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter'],
    ['Shift','z','x','c','v','b','n','m',',','.','/','Shift'],
    ['Space']
]    

uppercase = False  # use uppercase chars. 

def select(entry, value):
    global uppercase

    if value == "Space":
        value = ' '
    elif value == 'Enter':
        value = '\n'
    elif value == 'Tab':
        value = '\t'
        
    if value == "Backspace":
        if isinstance(entry, tk.Entry):
            entry.delete(len(entry.get())-1, 'end')
        #elif isinstance(entry, tk.Text):
        else: # tk.Text
            entry.delete('end - 2c', 'end')
    elif value in ('Caps Lock', 'Shift'):
        #print('Not implemented yet!')
        uppercase = not uppercase
    else:
        if uppercase:
            value = value.upper()
        entry.insert('end', value)

def create(root, entry):
    
    window = tk.Toplevel(root)
    window.configure(background="cornflowerblue")
    window.wm_attributes("-alpha", 0.7)

    for y, row in enumerate(alphabets):
        
        x = 0
        
        #for x, text in enumerate(row):
        for text in row:
         
            if text in ('Enter', 'Shift'):
                width = 15
                columnspan = 2
            elif text == 'Space':
                width = 130
                columnspan = 16
            else:                
                width = 5
                columnspan = 1

            tk.Button(window, text=text, width=width, 
                      command=lambda value=text: select(entry, value),
                      padx=3, pady=3, bd=12, bg="black", fg="white"
                     ).grid(row=y, column=x, columnspan=columnspan)

            x += columnspan
           
# --- main ---

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Test Keyboard')
    
    label = tk.Label(root, text='Test Keyboard')
    label.grid(row=0, column=0, columnspan=2)
    
    entry1 = tk.Entry(root)
    entry1.grid(row=1, column=0, sticky='news')

    button1 = tk.Button(root, text='Keyboard', command=lambda:create(root, entry1))
    button1.grid(row=1, column=1, sticky='news')

    entry2 = tk.Entry(root)
    entry2.grid(row=2, column=0, sticky='news')

    button2 = tk.Button(root, text='Keyboard', command=lambda:create(root, entry2))
    button2.grid(row=2, column=1, sticky='news')

    text1 = tk.Text(root)
    text1.grid(row=3, column=0, sticky='news')

    button3 = tk.Button(root, text='Keyboard', command=lambda:create(root, text1))
    button3.grid(row=3, column=1, sticky='news')

    root.mainloop()


