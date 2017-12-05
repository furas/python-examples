#!/usr/bin/env python3

import tkinter as tk

def callback():
    print('  root.geometry:', root.winfo_geometry())
    print('canvas.geometry:', canvas.winfo_geometry())
    print('canvas.width :', canvas.winfo_width())
    print('canvas.height:', canvas.winfo_height())
    print('canvas.x:', canvas.winfo_x())
    print('canvas.y:', canvas.winfo_y())
    print('canvas.rootx:', canvas.winfo_rootx())
    print('canvas.rooty:', canvas.winfo_rooty())
    
root = tk.Tk()

tk.Label(root, text='SOME WIDGETS IN ROOT').pack()

frame = tk.Frame(root)
frame.pack()
tk.Label(frame, text='SOME WIDGETS IN FRAME').pack()

canvas = tk.Canvas(frame, bg='green')
canvas.pack()

print('\n--- before mainloop start ---\n')
callback()

print('\n--- after mainloop start ---\n')
root.after(100, callback)

root.mainloop()
