import tkinter as tk
import subprocess

'''Command takes some time so it freezes GUI'''

# --- functions ---

def ping():
    # without `shell=True` - cmd as list
    cmd = ["ping", "-c", "2", entry.get()]
    output = subprocess.check_output(cmd)

    # with `shell=True` - cmd as string 
    #cmd = "ping -c 2 {}".format(entry.get())
    #output = subprocess.check_output(cmd, shell=True)

    result.insert('end', output.decode('utf-8'))

# --- main ---
    
root = tk.Tk()

l = tk.Label(root, text="Enter IP or host")
l.pack() 

entry = tk.Entry(root, textvariable=entry)
entry.pack()

b = tk.Button(root, text="RUN", command=ping)
b.pack() 

result = tk.Text(root)
result.pack()

root.mainloop()
