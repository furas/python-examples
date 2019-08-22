
# date: 2019.08.20

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A': [1,2,3],
    'B': [2,3,1],
    'C': [2,1,3],
})

figure, axes = plt.subplots(3,1)

df['A'].plot(ax=axes[0])
df['B'].plot(ax=axes[1])
df['C'].plot(ax=axes[2])

plt.show()


