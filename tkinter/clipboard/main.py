import tkinter as tk

root = tk.Tk()


root.clipboard_clear()

try:
    print('clipboard:', root.clipboard_get())
except Exception as ex:
    print('clipboard is empty or object is not string')
    print('ERROR:', ex)

root.clipboard_clear()
root.clipboard_append("Hello ")
root.clipboard_append("World")

try:
    print('clipboard:', root.clipboard_get())
except Exception as ex:
    print('ERROR:', ex)
    print('clipboard is empty or object is not string')
    print('ERROR:', ex)

root.done()
