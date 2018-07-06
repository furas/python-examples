# Clipboard in Tkinter


You can clean, get or append to `clipboard`

```python
root.clipboard_clear()
root.clipboard_append("Hello ")
root.clipboard_append("World")
print('clipboard:', root.clipboard_get()) 
# clipboard: Hello World
```

`Clipboard` can rise exception so you can use

```python
try:
    print('clipboard:', root.clipboard_get())
except Exception as ex:
    print('clipboard is empty or object is not string')
    print('ERROR:', ex)
```

`Clipboard` can use `type=` to set data type and then you can't get them using differnt `type`. As default it use `"STRING"` type


```python
root.clipboard_clear()
root.clipboard_append("Hello")
root.clipboard_append("World", type="IMAGE")

print('clipboard:', root.clipboard_get(type="IMAGE")) 
# clipboard: World   # it skiped "Hello"

print('clipboard:', root.clipboard_get()) 
# clipboard: Hello   # it skiped "World"
```
