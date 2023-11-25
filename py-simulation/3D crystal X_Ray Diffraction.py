# 3D Crystal X_Ray diffraction:

import numpy as np
from vpython import *
canvas(title='3D Crystal X_Ray diffraction:', width=1500, height=700, background=color.black)

(a, b, c) = (1, 1, 1)       # λ = a/5, b/5, c/5

# x_axis:
curve(vector(-6, 0, 0), vector(5, 0, 0))
curve(vector(0, -6, 0), vector(0, 5, 0))
curve(vector(0, 0, -6), vector(0, 0, 5))

# λ = a/10
al1 = np.arccos(3/5)           # n=1
bt1 = np.arccos(3/5)           # n=1
gm1 = np.arccos(1/10+1/2**0.5)  # n=1
al2 = np.arccos(7/10)           # n=2
bt2 = np.arccos(7/10)           # n=2
gm2 = np.arccos(1/5+1/2**0.5)   # n=2
for i in range(-3, 1):
    for j in range(0, 3):
        for k in range(-3, 1):
            sphere(pos=vector(a*i, b*j, c*k), radius=0.1, color=color.cyan)
    curve(vector((a*i-1/2**0.5), -1/2**0.5, -1), vector(a*i, 0, 0), color=color.yellow)
    curve(vector(a*i, 0, 0), vector(a*i+1, 0, 1*np.tan(al1)), color=color.red)
    curve(vector(a*i, 0, 0), vector(a*i+1*np.tan(bt1), 1, 0), color=color.green)
    curve(vector(a*i, 0, 0), vector(a*i, 1*np.tan(gm1), 1), color=color.blue)

l = 2
(xr1, xr2) = (l*np.tan(al1), l*np.tan(al2))
(yr1, yr2) = (l*np.tan(bt1), l*np.tan(bt2))
(zr1, zr2) = (l*np.tan(gm1), l*np.tan(gm2))

cone(pos=vector(l, 0, 0), axis=vector(-l, 0, 0), radius=xr1, opacity=0.2, color=color.red)
# cone(pos=vector(l, 0, 0), axis=vector(-l, 0, 0), radius=xr2, opacity=0.25, color=color.red)
cone(pos=vector(0, l, 0), axis=vector(0, -l, 0), radius=yr1, opacity=0.2, color=color.green)
# cone(pos=vector(0, l, 0), axis=vector(0, -l, 0), radius=yr2, opacity=0.25, color=color.green)
cone(pos=vector(0, 0, l), axis=vector(0, 0, -l), radius=zr1, opacity=0.2, color=color.blue)
# cone(pos=vector(0, 0, l), axis=vector(0, 0, -l), radius=zr2, opacity=0.25, color=color.blue)

