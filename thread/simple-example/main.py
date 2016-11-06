#!/usr/bin/env python3

from threading import Thread
import time

# -----

def my_function(name, counter):
    for x in range(counter):
        print(name, x)
        time.sleep(0.5)

# -----

class MyThread(Thread):
    
    def run(self):
        my_function("Hello", 10)
        
# -----

thread = MyThread()
thread.start()

# -----

# args have to be tuple so for one argument `args=(10,)`

thread = Thread( target=my_function, args=("World", 10) )
thread.start()

