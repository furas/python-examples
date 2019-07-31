
# date: 2019.07.27
# 

import subprocess

code = "python3 -c 'a=input();b=input();print(\"name:\", a, b)'"

a = 'James'
b = 'Bond'

data = a + '\n' + b

# ---

cmd = "echo '{}' | {}".format(data, code)
#cmd = f"echo '{data}' | {code}"

p = subprocess.Popen(cmd, shell=True)

# ---

cmd = code

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
output = p.communicate(input=data.encode())
print('output:', output[0].decode())

# ---

cmd = "echo '{}' | {}".format(data, code)
#cmd = f"echo '{data}' | {code}"

p = subprocess.run(cmd, shell=True)

# ---

cmd = code

p = subprocess.run(cmd, shell=True, capture_output=True, input=data.encode())
print('output:', p.stdout.decode())
