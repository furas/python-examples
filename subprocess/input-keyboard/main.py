
# date: 2019.07.27
# 

import subprocess

p = subprocess.Popen("echo 'James\nBond' | python3 -c 'a=input();b=input();print(\"name:\", a, b)'", shell=True)

p = subprocess.Popen("python3 -c 'a=input();b=input();print(\"name:\", a, b)'", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
output = p.communicate(input='James\nBond'.encode())
print('output:', output[0].decode())

p = subprocess.run("echo 'James\nBond' | python3 -c 'a=input();b=input();print(\"name:\", a, b)'", shell=True)

p = subprocess.run("python3 -c 'a=input();b=input();print(\"name:\", a, b)'", shell=True, capture_output=True, input='James\nBond'.encode())
print('output:', p.stdout.decode())
