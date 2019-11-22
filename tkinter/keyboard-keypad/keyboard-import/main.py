import tkinter as tk
import keyboard
           
# --- main ---

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello World!')
    
    label = tk.Label(root, text='Form')
    label.grid(row=0, column=0, columnspan=3)

    #-----    

    label1 = tk.Label(root, text='Entry 1')
    label1.grid(row=1, column=0)
    
    entry1 = tk.Entry(root)
    entry1.grid(row=1, column=1, sticky='news')

    button1 = tk.Button(root, text='Keyboard', command=lambda:keyboard.create(root, entry1))
    button1.grid(row=1, column=2, sticky='news')

    #-----    

    label2 = tk.Label(root, text='Entry 2')
    label2.grid(row=2, column=0)

    entry2 = tk.Entry(root)
    entry2.grid(row=2, column=1, sticky='news')

    button2 = tk.Button(root, text='Keyboard', command=lambda:keyboard.create(root, entry2))
    button2.grid(row=2, column=2, sticky='news')

    #-----    

    label3 = tk.Label(root, text='Text 1')
    label3.grid(row=3, column=0)

    text1 = tk.Text(root)
    text1.grid(row=3, column=1, sticky='news')

    button3 = tk.Button(root, text='Keyboard', command=lambda:keyboard.create(root, text1))
    button3.grid(row=3, column=2, sticky='news')

    root.mainloop()


