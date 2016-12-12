#!/usr/bin/env python3

#
# https://docs.python.org/3/library/threading.html
#

import threading
import time

# --- classes ---

class ExampleThread(threading.Thread):

    def __init__(self, name, counter=10, sleep=0.5):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.sleep = sleep
        
    def run(self):
        for x in range(self.counter):
            print(self.name, x)
            time.sleep(self.sleep)

# --- functions ---

def example_function(name, counter=10, sleep=0.5):
    for x in range(counter):
        print(name, x)
        time.sleep(sleep)


# --- example 1 ---

# `args` have to be tuple.
# for one argument you need `args=("function:",)`

t1 = threading.Thread(target=example_function, args=("function:", 15))
t1.start()

# --- example 2 ---

t2 = ExampleThread("class:", 10, 1.0)
t2.start()

# --- example 2 ---

# start thread after 3 seconds

t3 = threading.Timer(3, example_function, args=("** timer **:", 2, 3.0))
t3.start()


