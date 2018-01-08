
## Using Label 

See: main.py

You have to use label with image as parent for other widgets to put them inside this label.

Because it use `grid()` so you use `weight` to automatically resize empty rows and columns around widgets and they will be in the center.

![#1](images/tkinter-center-on-image.png?raw=true)   

As you see widgets have gray background which you can't remove. If you need text without gray background then you have to use [Canvas](http://effbot.org/tkinterbook/canvas.htm) with [create_text()](http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_text-method) (and [create_window()](http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_window-method) to put `Entry`)

---

## Using Canvas 

See: main-canvas.py

![#1](images/tkinter-canvas.png?raw=true)   
