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
        self.size = os.stat(path).st_size # remeber previous size

    def on_modified(self, event):
        #print(event)
        #print('path:', event.src_path)
        if event.src_path == self.path:
            new_size = os.stat(self.path).st_size
            #print('size:', self.size, new_size)
            if new_size > self.size: 
                fh = open(self.path)
                fh.seek(self.size) # move to appended content
                print(fh.read())
                fh.close()
                self.size = new_size        

        
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
    
