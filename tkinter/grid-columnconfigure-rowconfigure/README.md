
# Tkinter - grid() - rowconfigure() / columnconfigure()

```python
import tkinter as tk

root = tk.Tk()

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-01.png?raw=true)   

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-02.png?raw=true)   

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

![#1](images/main-03.png?raw=true)   

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

![#1](images/main-04.png?raw=true)   

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

![#1](images/main-05.png?raw=true)   

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

![#1](images/main-06.png?raw=true)   

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

| without<br/>`geometry()` | with<br/>`geometry('300x300')` |
| --- | --- |
|![#1](images/main-03.png?raw=true) | ![#1](images/main-05.png?raw=true) |

---

```python
import tkinter as tk

root = tk.Tk()
root.minsize(width=600, height=0)

root.columnconfigure(1, minsize=50, weight=1)
root.columnconfigure(3, minsize=50, weight=1)
root.rowconfigure(1, minsize=50, weight=1)
root.rowconfigure(3, minsize=50, weight=1)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

![#1](images/main-07.png?raw=true)

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

root.columnconfigure(1, weight=1)
root.columnconfigure(3, minsize=25) #weight=0
root.rowconfigure(1, weight=1)
root.rowconfigure(3, minsize=25) #weight=0

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
```

| at start |
| --- |
| ![#1](images/main-08.png?raw=true) |

| resized (using mouse) |
| --- |
| ![#1](images/main-09.png?raw=true) |

---

```python
import tkinter as tk

root = tk.Tk()
root.geometry('800x50')

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=4)
root.columnconfigure(3, weight=8)

b1 = tk.Button(root, text="Col 1")
b1.grid(column=1, row=1, stick='we')

b2 = tk.Button(root, text="Col 2")
b2.grid(column=2, row=1, stick='we')

b3 = tk.Button(root, text="Col 3")
b3.grid(column=3, row=1, stick='we')

root.mainloop()
```

![#1](images/main-10.png?raw=true)


---

```python
import tkinter as tk

root = tk.Tk()

root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=4)
root.rowconfigure(3, weight=8)

b0 = tk.Button(root, text="weight=0")
b0.grid(column=0, row=0, stick='ns')

b1 = tk.Button(root, text="weight=1")
b1.grid(column=0, row=1, stick='ns')

b2 = tk.Button(root, text="weight=4")
b2.grid(column=0, row=2, stick='ns')

b3 = tk.Button(root, text="weight=8")
b3.grid(column=0, row=3, stick='ns')

root.mainloop()
```

| at start |
| --- |
| ![#1](images/main-11.png?raw=true) |

| resized (using mouse) |
| --- |
| ![#1](images/main-12.png?raw=true) |

