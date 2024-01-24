'''
Vpython model: 1D Crystal X_Ray diffraction

Author : Anik Mandal
'''

import numpy as np
from vpython import *
canvas(title='1D Crystal X_Ray diffraction:', width=1500, height=700, background=color.black)

(a, b, c) = (1, 1, 1)       # λ = a/5, b/5, c/5

# x_axis:
curve(vector(-6, 0, 0), vector(5, 0, 0))

al1 = np.arccos(0.7)           # λ = a/5, n=1
al2 = np.arccos(0.9)           # λ = a/5, n=2

for i in range(-5, 1):
    sphere(pos=vector(a*i, 0, 0), radius=0.1, color=color.cyan)
    curve(vector(a*i-1, -2, 0), vector(a*i, 0, 0), color=color.yellow)
    curve(vector(a*i, 0, 0), vector(a*i+2, 2*np.tan(al1), 0), color=color.red)

curve(vector(a*0, 0, 0), vector((a*0)+2, 2*np.tan(al2), 0),color=color.red)

cone(pos=vector(2, 0, 0), axis=vector(-2, 0, 0), radius=2*np.tan(al1), opacity=0.25, color=color.red)
cone(pos=vector(2, 0, 0), axis=vector(-2, 0, 0), radius=2*np.tan(al2), opacity=0.4, color=color.red)


