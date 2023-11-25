

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

rr = []
th = []
fh = []

for i in range(1000):
    r = 2
    t = np.cos(i*0.01)
    f = np.sin(i*0.01)
    rr.append(r)
    th.append(t)
    fh.append(f)

xx = []
yy = []
zz = []

for i in range(len(rr)):
    xi = rr[i]*np.sin(th[i])*np.cos(fh[i])
    yi = rr[i]*np.sin(th[i])*np.sin(fh[i])
    zi = rr[i]*np.cos(th[i])
    xx.append(xi)
    yy.append(yi)
    zz.append(zi)

plt.plot(xx,yy,zz,'.r')
plt.show()
