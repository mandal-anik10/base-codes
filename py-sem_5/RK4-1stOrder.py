# RK4 Method: for 1st order

import numpy as np
import matplotlib.pyplot as plt

def yp(x, y):
    p = 2*x            # Function
    return p

# condition:
x0 = 0
y0 = 0

(xi, xf, n) = (x0, 5, 129)
h = abs(xf-xi)/(n-1)

xn = x0
yn = y0

xx = [x0]
yy = [y0]

for i in range(1, n):
    ypn = yp(xn, yn)
    k1 = h*ypn
    
    xn2 = xn + h/2
    yn2 = yn + k1/2
    ypn = yp(xn2, yn2)
    k2 = h*ypn

    xn3 = xn2
    yn3 = yn + k2/2
    ypn = yp(xn3, yn3)
    k3 = h*ypn

    xn4 = xn + h
    yn4 = yn + k3
    ypn = yp(xn4, yn4)
    k4 = h*ypn
    
    k = (k1+k2*2+k3*2+k4)/6
    xn = xi + i*h
    yn = yn + k

    xx.append(xn)
    yy.append(yn)

plt.plot(xx, yy)
plt.grid()
plt.show()
