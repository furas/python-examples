Using `command=` in `OptionMenu` you can assign function which will get selected value when you change selection.

    import tkinter as tk
    
    #--- functions ---
    
    def on_select(text):
        print('text:', text)
        print('---')
    
    #--- main ---
        
    data = ['a,b,c', 'x,y,z']
        
    root = tk.Tk()
    
    for i, options in enumerate(data):
        options = options.split(',')
        op = tk.OptionMenu(root, tk.StringVar(), *options, command=on_select)
        op.pack()
        
    root.mainloop()

`command=` in `Button` expected function which doesn't get parameters - ie. `def on_select():` but `command=` in `OptionMenu` expects function which gets single parameter - ie. `def on_select(text):`

This code doesn't need `variable = tk.StringVar()` 

---

So you have selected value but you don't know in which `OptionMenu` it was selected - in first or second. Using `lambda` you can assign function which will get more parameters and you can put number as second parameter. 

    import tkinter as tk
    
    #--- functions ---
    
    def on_select(text, number):
        print('text:', text)
        print('number:', number)
        print('data[number]:', data[number])
        print('---')
    
    #--- main ---
        
    data = ['a,b,c', 'x,y,z']
        
    root = tk.Tk()
    
    for i, options in enumerate(data):
        options = options.split(',')
        op = tk.OptionMenu(root, tk.StringVar(), *options, command=lambda text, number=i:on_select(text, number))
        op.pack()
        
    root.mainloop()

So now first OptionMenu runs `on_select(text, 0)` and second runs  `on_select(text, 1)` so function knows which OptionMenu was selected and it can get correct values from data (or do other things)

---

You can also use `StringVar()` to get selected values. if you need all selected values then you have to create separated `StringVar` for every `OptionMenu` and keep on list. When you click button then you can use `for` loop with list of variables to get all selected values.

    import tkinter as tk
    
    #--- functions ---
    
    def on_click():
    	for number, var in enumerate(all_variables):
    		print(number, '| selected:', var.get(), '| all:', data[number])
    
    #--- main ---
    
    data = ['a,b,c', 'x,y,z']
    
    root = tk.Tk()
    
    all_variables = []
    
    for options in data:
        options = options.split(',')
        var = tk.StringVar()
        all_variables.append(var)
        op = tk.OptionMenu(root, var, *options)
        op.pack()
    
    b = tk.Button(root, text='OK', command=on_click)
    b.pack()
    
    root.mainloop()


