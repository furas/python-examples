
# date: 2019.07.22
# https://stackoverflow.com/questions/57137643/multiple-frames-using-tkinker

import tkinter as tk

root = tk.Tk()

# - main frame -

f1 = tk.Frame(root, width=800, height=600, bg='green')
f1.pack_propagate(False) # dont change size
f1.pack() # visible

label1 = tk.Label(f1, text='800x600')
label1.place(relx=0.5, rely=0.5, anchor='c')

button1 = tk.Button(f1, text="Show")
button1.place(relx=1, rely=1, anchor='se')

# - bottom frame -

f2 = tk.Frame(root, width=800, height=230, bg='red')
f2.pack_propagate(False) # dont change size
#f2.pack() # hidden 

label2 = tk.Label(f2, text='800x230')
label2.place(relx=0.5, rely=0.5, anchor='c')

button2 = tk.Button(f2, text="Close", command=f2.pack_forget) # function to hide
button2.place(relx=1, rely=1, anchor='se')

# - assign function from bottom-frame to button in main-frame

button1['command'] = f2.pack # function to show

# -

root.mainloop()   
