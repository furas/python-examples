
# date: 2019.08.26
# https://stackoverflow.com/questions/57661001/how-can-i-plot-a-graph-like-this-one-in-python
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

import matplotlib.pyplot as plt
import numpy as np

def u_0(x):
    a = 1.0/np.cosh(2.0*(x+8.0))
    b = 1.0/np.cosh((x+1.0))
    return 8.0*a*a + 2.0*b*b

# spatial grid
N = 100
x = np.linspace(-10, 10, N)

# time
Nt = 100
tlist = np.linspace(0.0, 2.0, Nt)

#velocity
c = 5.0
count = 0

for t in tlist:
  u = u_0(x-c*t)
  u += count  # offset 
  plt.plot(x, u)
  count += 1

plt.savefig("result_2D.png")
plt.show()

