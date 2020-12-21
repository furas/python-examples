#!/usr/bin/env python3

eval('print(open("/etc/passwd").read())')
#eval("print(open('/etc/shadow').read())") # restricted 

eval('print(2*PI*r)', {'r': 2, 'PI': 3.1415})

eval('exec("import sys; print(sys.path)")')

eval('exec(\'import os; print("\\\\n".join(os.listdir()))\')')

# console ???

#eval('__import__("os").execve("/bin/sh",["?"],{})') # shell sh
eval('__import__("os").execve("/bin/bash",["?"],{})') # shell bash
