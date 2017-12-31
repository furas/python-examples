#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48043714/1832058
#

data = [
    [0, 1, 100, 758.2],
    [0, 1, 100, 1738.1],
    [0, 1, 100, 752.2],
    [0, 1, 100, 868.9],
    [0, 1, 100, 742.3],
]

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create dataframe
df = pd.DataFrame(data).T

# create mesh 5x4
Y = range(df.shape[0])
X = range(df.shape[1])
X, Y = np.meshgrid(X, Y)

# draw it
threedee = plt.figure().gca(projection='3d')
threedee.plot_wireframe(X, Y, df)

# show it
plt.show()
