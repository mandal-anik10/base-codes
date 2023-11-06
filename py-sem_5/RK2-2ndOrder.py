# RK2 method: for 2nd order
import numpy as np
import matplotlib.pyplot as plt

def y2p(x, y, y_p):
    p2 = -0*y_p - 100*y          # Function
    return p2
    
# condition:
x0 = 0
y0 = 0
yp0 = 2

y2p0 = y2p(x0, y0, yp0)
(xi, xf, n) = (x0, 3, 1+2**7)
h = abs(xf-xi)/(n-1)

xn = x0
yn = y0
ypn = yp0
y2pn = y2p0

xx = [x0]
yy = [y0]

for i in range(1, n):
    k1 = h*ypn
    
    xn2 = xn + h
    yn2 = yn + k1
    ypn = ypn + y2pn*h
    y2pn = y2p(xn2, yn2, ypn)
    k2 = h*ypn
    
    k = (k1+k2)/2
    yn = yn + k
    xn = xi + i*h
    
    xx.append(xn)
    yy.append(yn)

plt.plot(xx, yy)
plt.grid()
plt.show()
