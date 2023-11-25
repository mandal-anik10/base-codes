# IVP: Euler's method for solving 2nd order ODE:

import numpy as np
import matplotlib.pyplot as plt

# y'' + 2b *y' + w**2 * y = f(x)    let, b = 1, w = 0.5, f(x) = 0

# conditions:
t0 = 0
y0 = 0
yp0 = 2
b = 5
f = 100     # w**2

ti = t0
tf = 3
n = 1+2**17
h = (tf-ti)/(n-1)
yi = y0
ypi = yp0
y2pi = -2*b*ypi-f*yi

tt = [t0]
yy = [y0]

for i in range(1, n):
    ti = ti + h
    yi = yi + h*ypi
    ypi = ypi + h*y2pi
    y2pi = -2 * b * ypi - f * yi

    tt.append(ti)
    yy.append(yi)

plt.plot(tt, yy)
plt.grid()
plt.show()

