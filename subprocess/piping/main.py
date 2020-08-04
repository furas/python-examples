
# author: https://blog.furas.pl
# date: 2020.07.31
# link: https://stackoverflow.com/questions/63187482/python-sub-process-module-reading-and-writing-at-the-same-time

import subprocess
import os

def version1_shell():

    p = subprocess.Popen('cat ~/.bashrc | grep export', stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version2_shell():
    path = os.path.expanduser('~/.bashrc')
    
    p = subprocess.Popen('grep export', stdin=open(path, 'r'), stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version3_shell():
    path = os.path.expanduser('~/.bashrc')
    
    data = open(path, 'rb').read()
    
    p = subprocess.Popen('grep export', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate(data)

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version4_shell():
    p1 = subprocess.Popen('cat ~/.bashrc', stdout=subprocess.PIPE, shell=True)    
    p2 = subprocess.Popen('grep export', stdin=p1.stdout, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p2.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
    
def version1():
    ''' doesn't work `~` but it can be replaced with full path '''
    ''' doesn't work `|` and it can't be replaced '''
    
    ''' DOESN"T WORK '''
    
    path = os.path.expanduser('~/.bashrc')

    #p = subprocess.Popen(['cat', '~/.bashrc', '|', 'grep', 'export'], stdout=subprocess.PIPE)
    p = subprocess.Popen(['cat', path, '|', 'grep', 'export'], stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version2():
    path = os.path.expanduser('~/.bashrc')
    
    p = subprocess.Popen(['grep', 'export'], stdin=open(path, 'r'), stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version3():
    path = os.path.expanduser('~/.bashrc')
    
    data = open(path, 'rb').read()
    
    p = subprocess.Popen(['grep', 'export'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(data)

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

def version4():
    ''' doesn't work `~` but it can be replaced with full path '''

    path = os.path.expanduser('~/.bashrc')

    #p1 = subprocess.Popen(['cat', '~/.bashrc'], stdout=subprocess.PIPE)    
    p1 = subprocess.Popen(['cat', path], stdout=subprocess.PIPE)    
    p2 = subprocess.Popen(['grep', 'export'], stdin=p1.stdout, stdout=subprocess.PIPE)
    stdout, stderr = p2.communicate()

    if stdout:    
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

#version1_shell()  # OK
#version2_shell()  # OK
#version3_shell()  # OK
#version4_shell()  # OK

#version1()  # DOESN'T WORK - it has to use two processes like in version4
#version2()  # OK
#version3()  # OK
#version4()  # OK
    
    
