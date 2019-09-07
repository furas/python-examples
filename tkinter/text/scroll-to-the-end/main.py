
# date: 2019.08.27
# scroll Text to last line 
import tkinter as tk

root = tk.Tk()

t = tk.Text()
t.pack()

for x in range(100):
    t.insert('end', '{}\n'.format(x))
    
t.yview_moveto(1)
#t.yview_scroll(100, 'units') # 100 lines

root.mainloop()
