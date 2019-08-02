import tkinter as tk
from pynput import mouse

def onMouseClick(*args):
    print(args)

def on_start():
    global listener

    if not listener:
        print("Start listener...")
        listener = mouse.Listener(on_click=onMouseClick)
        listener.start() # start thread
    else:
        print("listener already running")

def on_stop():
    global listener

    if listener:
        print("Stop listener...")
        listener.stop()  # stop thread
        listener.join()  # wait till thread really ends its job
        listener = None  # to inform that listener doesn't exist
    else:
        print("listener not running")

if __name__ == "__main__" :

    print("Starting...")

    listener = None  # to keep listener

    root = tk.Tk()

    btn = tk.Button(root, command=on_start, text="Star Mouse Listener")
    btn.pack()

    btn = tk.Button(root, command=on_stop, text="Stop Mouse Listener")
    btn.pack()

    root.mainloop()

    # stop listener if it was created
    if listener: # if listener is not None:
        print("Stop listener...")
        listener.stop()  # stop thread
        listener.join()  # wait till thread really ends its job
