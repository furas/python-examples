#!/usr/bin/env python3

#
# create virtual ports
#
# $ sudo apt install socata
#
# $ socat -d -d pty,raw,echo=0 pty,raw,echo=0
#
# 2016/11/13 16:33:30 socat[18425] N PTY is /dev/pts/5
# 2016/11/13 16:33:30 socat[18425] N PTY is /dev/pts/6
# 2016/11/13 16:33:30 socat[18425] N starting data transfer loop with FDs [3,3] and [5,5]
#
# It creates ports /dev/pts/5 and /dev/pts/6
#
# You read from /dev/pts/6
#
# $ cat < /dev/pts/6
#
# You write to /dev/pts/5
#
# $ echo "Hello" > /dev/pts/5
#

import tkinter as tk
import serial 

# --- functions ---

def readserial():
    b = ser.readline()
    if b.strip():
         label['text'] = b.decode('utf-8').strip()
    # run again after 100ms (mainloop will do it)
    root.after(100, readserial)
    
# --- main ---

#ser = serial.Serial(port='COM4', baudrate=9600, timeout=1)
ser = serial.Serial(port='/dev/pts/6', baudrate=9600, timeout=1)

root = tk.Tk()

label = tk.Label(root)
label.pack()

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

# run readserial first time after 100ms (mainloop will do it)
root.after(100, readserial)

# start GUI
root.mainloop()
