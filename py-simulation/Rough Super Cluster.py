
import numpy as np
import matplotlib.pyplot as plt
import time

t1 = time.time()

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.set_aspect("equal")
ax2.set_aspect("equal")

n = 5000

xx = []
yy = []
pixel_n = 200
D = np.zeros([pixel_n+2, pixel_n+2])

for i in range(n):
    x = np.random.random()
    y = np.random.random()
    xx.append(x)
    yy.append(y)

ax1.plot(xx, yy, '.k')
ax1.grid()

f = 1/pixel_n
for j in range(pixel_n):
    for k in range(pixel_n):
        count = 0
        for i in range(n):
            if (f*j <= xx[i] < f*(j+1)) and (f*k <= yy[i] < f*(k+1)):
                count = count + 1
        D[k+1][j+1] = count

map = ax2.imshow(D, cmap="afmhot")
fig.colorbar(map)

t2 = time.time()
print("Simulation time : ", (t2-t1)/60, "min")

plt.show()
