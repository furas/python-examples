#!/usr/bin/env python3

# date: 2019.09.23
# https://stackoverflow.com/questions/58055480/python-how-to-get-log-append-content/

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AppendEventHandler(FileSystemEventHandler):

    def __init__(self, path):
        self.path = path
        self.fh = open(path)

    def on_modified(self, event):
        print(dir(event))
        #print('path:', event.src_path)
        if event.src_path == self.path:
            print(self.fh.read())

        
if __name__ == "__main__":
    event_handler = AppendEventHandler("./test.log")
    
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
