# Spherical Harmonics: Try-1

from LocalModule.Basic import *
from matplotlib.pyplot import *
from numpy import *

fig = figure()
ax = fig.add_subplot(111, projection="3d")

rr = []
theta = linspace(0, 2 * pi, 25)
phi = linspace(0, 2 * pi, 25)

xx = []
yy = []
zz = []

FR = []
FI = []

# input
l = 3
m = 2
norm = ((4 * np.pi / (2 * l + 1)) * (Fact(l + abs(m), 1, 1) / Fact(l - abs(m), 1, 1))) ** 0.5


def f(num):
    fun = 15 * num * (1 - num ** 2) ** 1.0
    return fun


for i in range(len(theta)):
    for j in range(len(phi)):
        fr = f(cos(theta[i])) * cos(m * phi[j]) / norm
        fi = f(cos(theta[i])) * sin(m * phi[j]) / norm
        FR.append(fr)
        FI.append(fi)
Mr = max(FR)
Mi = max(FI)
mr = min(FR)
mi = min(FI)

for i in range(len(theta)):
    for j in range(len(phi)):
        r = 2
        rr.append(r)
        x = r * cos(theta[i]) * cos(phi[j])
        y = r * cos(theta[i]) * sin(phi[j])
        z = r * sin(theta[i])
        # xx.append(x)
        # yy.append(y)
        # zz.append(z)
        fr = f(cos(theta[i])) * cos(m * phi[j]) / norm
        fi = f(cos(theta[i])) * sin(m * phi[j]) / norm
        cr = abs((fr - mr) / (Mr - mr))
        cb = abs((fi - mi) / (Mi - mi))
        ax.scatter(x, y, z, color=(cr, 0, cb))
show()
