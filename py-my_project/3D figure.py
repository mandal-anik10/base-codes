import random

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

for k in range(0, 1000, 1):
    a = np.linspace(0, 20, 100)
    x = np.sin(a)
    y = np.cos(a)
    z = random.uniform(0, 3)
    if z > 2:
        ax.plot(x, y, z, "orange")
    elif z < 1:
        ax.plot(x, y, z, 'g')
    else:
        ax.plot(x, y, z, 'w')
plt.show()
