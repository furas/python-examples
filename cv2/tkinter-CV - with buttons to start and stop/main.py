#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk
import cv2

# --- functions ---

def play():
    '''
    start stream (run_camera and update_image) 
    and change state of buttons
    '''
    
    global run_camera

    if not run_camera:
        run_camera = True
        
        button_play['state'] = 'disabled'
        button_stop['state'] = 'normal'
        
        update_image()

def stop():
    '''
    stop stream (run_camera) 
    and change state of buttons
    '''
    global run_camera

    if run_camera:
        run_camera = False

        button_play['state'] = 'normal'
        button_stop['state'] = 'disabled'

def update_image():
    '''executed frequencally, it updates frame/image on canvas'''

    # read one frame (and "return" status)
    ret, frame = cap.read()

    if ret is None:
        print("Can't read from camera")
    else:
        image = Image.fromarray(frame)
        photo.paste(image)

    if run_camera:
        root.after(10, update_image)

def save_image():
    '''save current frame in file'''
    
    image.save('output.png')
          
# --- main ---

# open stream
cap = cv2.VideoCapture(0) # local (built-in) camera

# check if opened 
if not cap.isOpened():
    print("Can't open camera")
    cap.release()
    exit(1)

# get first frame
ret, frame = cap.read()

if ret is None:
    print("Can't read from camera")
    cap.release()
    exit(1)

# ---

# control stream on canvas
run_camera = False 
          
# ---

root = tk.Tk()

image = Image.fromarray(frame)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
canvas.pack(fill='both', expand=True)

canvas.create_image((0,0), image=photo, anchor='nw')

# ---

buttons = tk.Frame(root)
buttons.pack(fill='x')

button_play = tk.Button(buttons, text="Play", command=play)
button_play.pack(side='left')

button_stop = tk.Button(buttons, text="Stop", command=stop, state='disabled')
button_stop.pack(side='left')

button_save = tk.Button(buttons, text="Save Image", command=save_image)
button_save.pack(side='left')

# ---

root.mainloop()

# ---

# close stream
cap.release()

