
# date: 2019.08.20

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A': [1,2,3],
    'B': [2,3,1],
    'C': [2,1,3],
})

axes = df[['A','B', 'C']].plot(subplots=True)

plt.show()
