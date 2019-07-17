
# date: 2019.07.08
# https://stackoverflow.com/questions/56925820/function-to-start-and-stopthread/56926749#56926749


from pynput.keyboard import Listener, Key
import tkinter as tk
from functools import partial


def press(key):
    keyd = str(key)
    keyd = keyd.replace("Key.space", " ")
    keyd = keyd.replace("'", "")

    with open("doc.txt", "a") as o:
        o.write(keyd)
        print("key:", keyd)

    # key combination to stop listener (and end thread)
    #if key == Key.esc:
    #    return False


def startListener(arg):
    global listener # inform function to use external variable

    if arg == btStart:
        if listener is None:
            print('[+] starting listener')
            listener = Listener(on_press=press)
            listener.start()
        else:
            print('[!] already running')

    if arg == btStop:
        if listener is None:
            print('[!] not running')
        else:
            print('[+] stoping thread')
            listener.stop()
            listener.join()
            listener = None

# ---------------------------------------------------------

listener = None

app = tk.Tk()
app.geometry("300x100")

btStart = tk.Button(app, text="Start")
btStart.pack(side='top', fill='both', expand=True)
btStart["command"] = partial(startListener, btStart)

btStop = tk.Button(app, text="Stop")
btStop.pack(side='top', fill='both', expand=True)
btStop["command"] = partial(startListener, btStop)

app.mainloop()

