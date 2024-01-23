'''
Animation of Lissajous figure using Vpython

Author : Anik Mandal
'''

from vpython import *
import numpy as np

canvas(background = color.white)
p = sphere(pos = vector(0,0,0),radius = 0.5,color = color.red)

t = curve(color=color.cyan)
xa = curve(vector(-12,0,0),vector(12,0,0),color = color.black)
ya = curve(vector(0,-12,0),vector(0,12,0),color = color.black)
q = 1000
n = 2
m = 1.5
l = n*m
xy = np.linspace(-2*np.pi*l,2*np.pi*l,q)
xz = np.linspace(-2*np.pi*l,2*np.pi*l,q)

y = 10*np.sin(n*xy)
z = 10*np.sin(m*xz)
i = 0

while i < q:
    rate(100/l)
    p.pos = vector(y[i],z[i],0)
    t.append(p.pos)
    if i == q-1:
        i = 0
    i = i+1