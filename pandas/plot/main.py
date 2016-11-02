#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# some random data
import random
data = [ random.randint(-100, 100) for _ in range(100) ]


df = pd.DataFrame(data)

df.plot()

plt.show()
