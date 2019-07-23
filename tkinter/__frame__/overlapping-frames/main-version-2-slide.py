
# date: 2019.07.22
# https://stackoverflow.com/questions/57137643/multiple-frames-using-tkinker

import tkinter as tk

def move_in(event=None):
    y = int(f2.place_info()['y'])
    if y > 600:
        f2.place_configure(y=y-10)
        root.after(20, move_in)

def move_out(event=None):
    y = int(f2.place_info()['y'])
    if y < 600+230:
        f2.place_configure(y=y+10)
        root.after(20, move_out)
                 
# --- main ---

root = tk.Tk()
root.geometry('800x600')


f1 = tk.Frame(root, width=800, height=600, bg='green')
f1.place(x=0, y=0)

label1 = tk.Label(f1, text='800x600')
label1.place(relx=0.5, rely=0.5, anchor='c')


f2 = tk.Frame(root, width=800, height=230, bg='red')
f2.place(x=800, y=830, anchor='se')

label2 = tk.Label(f2, text='800x230')
label2.place(relx=0.5, rely=0.5, anchor='c')

button2 = tk.Button(f2, text="Close", command=move_out)
button2.place(relx=1, rely=1, anchor='se')


#button1 = tk.Button(f1, text="Show", command=lambda:f2.place(x=800, y=600, anchor='se'))
button1 = tk.Button(f1, text="Show", command=move_in)
button1.place(relx=1, rely=1, anchor='se')

root.mainloop()   
