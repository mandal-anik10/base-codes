'''
Vpython model : 2D Crystal X_Ray diffraction

Author : Anik Mandal
'''

import numpy as np
from vpython import *
canvas(title='2D Crystal X_Ray diffraction:', width=1500, height=700, background=color.black)

(a, b, c) = (1, 1, 1)       # λ = a/5, b/5, c/5

# x_axis:
curve(vector(-6, 0, 0), vector(5, 0, 0))
curve(vector(0, -6, 0), vector(0, 5, 0))
# λ = a/10
al1 = np.arccos(3/5)           # n=1
bt1 = np.arccos(3/5)           # n=1
al2 = np.arccos(7/10)           # n=2
bt2 = np.arccos(7/10)           # n=2

for i in range(-3, 1):
    for j in range(0, 3):
        sphere(pos=vector(a*i, b*j, 0), radius=0.1, color=color.cyan)
    curve(vector((a*i-1/2**0.5), -1/2**0.5, -1), vector(a*i, 0, 0), color=color.yellow)
    curve(vector(a*i, 0, 0), vector(a*i+1, 0, 1*np.tan(al1)), color=color.red)
    curve(vector(a*i, 0, 0), vector(a*i, 1, 1*np.tan(al1)), color=color.green)
l = 2
r1 = 2*np.tan(al1)
r2 = 2*np.tan(al2)
cone(pos=vector(l, 0, 0), axis=vector(-l, 0, 0), radius=r1, opacity=0.2, color=color.red)
cone(pos=vector(l, 0, 0), axis=vector(-l, 0, 0), radius=r2, opacity=0.25, color=color.red)
cone(pos=vector(0, l, 0), axis=vector(0, -l, 0), radius=r1, opacity=0.2, color=color.green)
cone(pos=vector(0, l, 0), axis=vector(0, -l, 0), radius=r2, opacity=0.25, color=color.green)

# intersect:

curve(vector(0, 0, 0), vector(2, 2, (r1**2-l**2)**0.5))
curve(vector(0, 0, 0), vector(2, 2, -(r1**2-l**2)**0.5))

curve(vector(0, 0, 0), vector(2, 2, (r2**2-l**2)**0.5))
curve(vector(0, 0, 0), vector(2, 2, -(r2**2-l**2)**0.5))

x1 = 2*((1+np.tan(bt2)**2)/(1+np.tan(al1)**2))**0.5
y1 = 2
z1 = (4*np.tan(bt2)**2-x1**2)**0.5
curve(vector(0, 0, 0), vector(x1, y1, z1))
curve(vector(0, 0, 0), vector(x1, y1, -z1))

x2 = 2
y2 = 2*((1+np.tan(al2)**2)/(1+np.tan(bt1)**2))**0.5
z2 = (4*np.tan(al2)**2-y2**2)**0.5
curve(vector(0, 0, 0), vector(x2, y2, z2))
curve(vector(0, 0, 0), vector(x2, y2, -z2))



