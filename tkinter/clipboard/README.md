# Clipboard in Tkinter


You can clean, get or append to `clipboard`

```python
root.clipboard_clear()
root.clipboard_append("Hello ")
root.clipboard_append("World")
print('clipboard:', root.clipboard_get()) 
# Hello World
```

`Clipboard` can rise exception so you can use

```python
try:
    print('clipboard:', root.clipboard_get())
except Exception as ex:
    print('clipboard is empty or object is not string')
    print('ERROR:', ex)
```

