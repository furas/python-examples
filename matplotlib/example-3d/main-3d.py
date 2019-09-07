
# date: 2019.08.26
# https://stackoverflow.com/questions/57661001/how-can-i-plot-a-graph-like-this-one-in-python
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # need for `projection=`
import numpy as np

def u_0(x):
    a = 1.0/np.cosh(2.0*(x+8.0))
    b = 1.0/np.cosh((x+1.0))
    return 8.0*a*a + 2.0*b*b

#velocity
c = 5.0

#spatial grid
N = 30
x = np.linspace(-10, 10, N)
t = np.linspace(0.0, 2.0, N)

X, T = np.meshgrid(x, t)
Y = u_0(X-c*T)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, T, Y)

plt.savefig('result_3D.png')
plt.show()

