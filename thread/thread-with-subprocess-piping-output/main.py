import threading
import time
import subprocess

def func1():
    while True:
        time.sleep(1)
        print('Hello')

def func2():
    p = subprocess.Popen(['ping', 'stackoverflow.com'], stdout=subprocess.PIPE)#, shell=True)#, stdout=sys.stdout
    for line in p.stdout:
        print('>>>', line.decode().strip())

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
