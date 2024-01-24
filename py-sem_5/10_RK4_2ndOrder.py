'''
RK4 method: for 2nd order

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt

def y2p(x, y, y_p):
    p2 = -10*y_p - 100*y            # ODE
    return p2
    
# condition:
x0 = 0
y0 = 0
yp0 = 2

y2p0 = y2p(x0, y0, yp0)
(xi, xf, n)=(x0, 3, 1+2**17)
h = abs(xf-xi)/(n-1)

xn = x0
yn = y0
ypn = yp0
y2pn = y2p0

xx = [x0]
yy = [y0]

for i in range(1, n):
    ypn1 = ypn
    k1 = h*ypn1
    
    xn2 = xn + h/2
    yn2 = yn + k1/2
    ypn2 = ypn + y2pn*h/2
    y2pn2 = y2p(xn2, yn2, ypn2)
    k2 = h*ypn2

    xn3 = xn + h/2
    yn3 = yn + k2/2
    ypn3 = ypn + y2pn*h/2
    y2pn3 = y2p(xn2, yn2, ypn3)
    k3 = h*ypn3

    xn4 = xn + h
    yn4 = yn + k3
    ypn4 = ypn + y2pn*h
    y2pn4 = y2p(xn2, yn2, ypn4)
    k4 = h*ypn4

    k = (k1+2*k2+2*k3+k4)/6
    xn = xi + i*h
    yn = yn + k
    ypn = ypn + y2pn*h
    y2pn = y2p(xn, yn, ypn)
    
    xx.append(xn)
    yy.append(yn)

plt.plot(xx, yy)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
