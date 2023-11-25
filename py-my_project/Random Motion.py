import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random as rd

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
(xc, yc, zc) = (0, 0, 0)
xx = []
yy = []
zz = []
for k in range(1000):
    xx.append(xc)
    yy.append(yc)
    zz.append(zc)

    r = rd.uniform(0, 1)
    phi = rd.uniform(0, 2*np.pi)
    theta = rd.uniform(0, np.pi)

    xc = r*np.sin(theta)*np.cos(phi)+xc
    yc = r*np.sin(theta)*np.sin(phi)+yc
    zc = r*np.cos(theta)+zc

ax.plot(xx, yy, zz, 'r', linewidth = "0.5")
ax.plot(xx, yy, zz, '.k', markersize= "1")
plt.title("Random Motion in 3D")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
