
#Tkinter - grid() - rowconfigure() / columnconfigure()

```python
import tkinter as tk

root = tk.Tk()

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-1.png?raw=true)   

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-2.png?raw=true)   
