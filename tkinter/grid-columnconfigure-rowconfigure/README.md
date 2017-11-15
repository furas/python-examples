
# Tkinter - grid() - rowconfigure() / columnconfigure()

```python
import tkinter as tk

root = tk.Tk()

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-1.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-2.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()

root.columnconfigure(1, minsize=50)
root.columnconfigure(3, minsize=50)
root.rowconfigure(1, minsize=50)
root.rowconfigure(3, minsize=50)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-3.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

root.columnconfigure(1, minsize=50)
root.columnconfigure(3, minsize=50)
root.rowconfigure(1, minsize=50)
root.rowconfigure(3, minsize=50)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-4.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-5.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
#root.geometry('300x300')

root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-6.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

root.columnconfigure(1, minsize=50, weight=1)
root.columnconfigure(3, minsize=50, weight=1)
root.rowconfigure(1, minsize=50, weight=1)
root.rowconfigure(3, minsize=50, weight=1)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

|with<br/>`geometry()`|without<br/>`geometry()`|
| --- | --- |
| ![#1](images/main-5.png?raw=true) | ![#1](images/main-3.png?raw=true) |


