#!/usr/bin/env python3

# date: 2020.02.20
# https://stackoverflow.com/questions/60318726/how-can-i-integrate-opencv-into-a-tkinter-window
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
# https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html

import tkinter as tk
from PIL import Image, ImageTk  #, ImageDraw, ImageFont
import cv2

# --- functions ---

def update_frame():

    ret, frame = cap.read()
    
    #frame = cv2.rectangle(frame, (280,200,80,80), color=(255,0,0), thickness=2)
    #frame = cv2.putText(frame, "Hello World!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255)) 
    
    image = Image.fromarray(frame)
    
    #image_draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    #image_draw.text((10,60), "Hello World!", font=font, fill=(255,255,255))
    #image_draw.rectangle((280,200,360,280), outline=(255,0,0), width=3)
    
    photo.paste(image) # copy image on photo

    #description['text'] = 'new text'
    
    root.after(40, update_frame) # update again after 40ms - it should give 25 FPS (1000ms/40ms = 25)

# --- main ---

cap = cv2.VideoCapture(0)

# get first frame to create photo
ret, frame = cap.read()

# - GUI -

root = tk.Tk()

image = Image.fromarray(frame)
photo = ImageTk.PhotoImage(image)  # it has to be after `tk.Tk()`

canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
canvas.pack(fill='both', expand=True)

image_id = canvas.create_image((0,0), image=photo, anchor='nw')

description = tk.Label(root, text="Place for description")
description.pack()

# - start -

update_frame() # update it first time

root.mainloop()  # run loop all time - it shows window

# - after close window -

# close stream
cap.release()
