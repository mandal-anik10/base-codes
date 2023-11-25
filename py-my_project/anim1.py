import random as rd

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = []
y = []

# fig=plt.figure()
# ai = fig.add_subplot(1,1,1,projection="3d")
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
# ai.set_zlim(-5,5)
line, = ax.plot(0, 0)


def AniF(i):
    x.append(rd.uniform(-5, 5))
    y.append(rd.uniform(-5, 5))
    line.set_xdata(x)
    line.set_ydata(y)
    return line,


ani = FuncAnimation(fig, func=AniF, frames=np.arange(0, 1, 1), interval=1)
plt.show()
