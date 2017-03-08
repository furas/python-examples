#!/usr/bin/env python3

from Xlib import display
import time

root = display.Display().screen().root

while True:
    data = root.query_pointer()._data
    x = data["root_x"]
    y = data["root_y"]
    print(x, y, end='\r')
    time.sleep(0.1)
