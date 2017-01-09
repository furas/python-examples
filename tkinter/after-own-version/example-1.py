#!/usr/bin/env python3
from __future__ import print_function
import time

# --- classes ---

class TaskManager():

    def __init__(self):
        # create dictionary for tasks
        self.tasks = dict()

        # set index of first task
        self.index = 0

        # lets run mainloop
        self.running = True

    def after(self, delay, callback):
        # get current time as milliseconds
        current_time = time.time()*1000

        # convert delay into time in the future
        run_time = current_time + delay

        # add task to the list
        self.index += 1
        self.tasks[self.index] = (run_time, callback)

        # return index of this task
        return self.index

    def after_cancel(self, index):
        # check if task still exists
        if index in self.tasks:
            # remove from list
            del self.tasks[index]

    def mainloop(self):

        # for sure lets run mainloop
        # (so you can run mainloop again without creating new instance)
        self.running = True

        while self.running:

            # get current time as milliseconds
            current_time = time.time()*1000

            # start checking all the tasks on list
            # Python 3 needs `list()` to create list from generator
            # because `del` changes oryginal list and generator raise error
            for key in list(self.tasks.keys()):
                # it has to check if `key` is still on this list
                # because it could be removed meanwhile by `del`
                if key in self.tasks:
                    # get task
                    run_time, callback = self.tasks[key]
                    # check if it is time to execute it
                    if current_time >= run_time:
                        # execute task
                        callback()
                        # remove from list
                        del self.tasks[key]

            # to not use all CPU
            time.sleep(0.1)

    def quit(self):
        # stop mainloop
        self.running = False

    def destroy(self):
        # stop mainloop
        self.running = False

# --- function ---

def hello():
    # inform function to use external/global variables
    # because we use `=` and `+=` with those variables
    global count
    global h_id

    print("hello", count)
    count += 1

    # run again after 1000ms = 1s
    h_id = root.after(1000, hello)

def stop_hello():
    # inform function to use external/global variables
    # because we use `=` and `+=` with those variables
    global s_id

    if count > 10:
        # remove `h_id` from list of jobs
        root.after_cancel(h_id)
        print("counting cancelled")
    else:
        # run again after 200ms = 0.2s
        s_id = root.after(200, stop_hello)

# --- main ---

# - global variables -

count = 0
h_id = None
s_id = None

# - GUI -

root = TaskManager()

# create two afters
h_id = root.after(1000, hello)  # time in ms, function
s_id = root.after(200, stop_hello)

# exit mainloop after 12s
root.after(12000, root.destroy)

# start the engine
root.mainloop()
