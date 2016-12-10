#!/usr/bin/env python3

import multiprocessing
import time


class Counter(object):

    def __init__(self):
        self.value = 0

    def update(self):
        self.value += 1


def job(counter, conn):
    
    while True:
        counter.update()
        
        # check if there is some message
        # (it doesn't block process and doesn't raise exception like recv() can do)
        if conn.poll():
            # receive message (it blocks program)
            print('job:', conn.recv())
            # send message
            conn.send(counter.value)


if __name__ == '__main__':
    # this part is executed only in main process
    # because it is inside `if __name__ == '__main__':`

    # create pipe with two endpoints
    conn_1, conn_2 = multiprocessing.Pipe()

    # create object which will be used in process
    counter = Counter()

    # create process, send one endpoint to process.
    # `args` has to be tuple - event it has only one argument
    p = multiprocessing.Process(target=job, args=(counter, conn_2)) 
    p.start()

    # work awhile
    time.sleep(2)

    # check value of the counter   
    conn_1.send('give me result')   # send message to process
    print('result:', conn_1.recv()) # receive message from process

    # end process
    p.terminate()
