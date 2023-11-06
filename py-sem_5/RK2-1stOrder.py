# RK2 method: for 1st order
import numpy as np
import matplotlib.pyplot as plt

def yp(x, y):
    p = 2*x        # Function
    return p

# condition:
x0 = 0
y0 = 0

yp0 = yp(x0, y0)
(xi, xf, n) = (x0, 3, 128)
h = abs(xf-xi)/(n-1)

xn = x0
yn = y0
ypn = yp0

xx = [x0]
yy = [y0]

for i in range(1,n):
    k1 = h*ypn
    xn2 = xn + h
    yn2 = yn + k1
    ypn = yp(xn2, yn2)
    k2 = h*ypn
    
    k = (k1+k2)/2
    yn = yn + k
    xn = xi + i*h
    
    xx.append(xn)
    yy.append(yn)

plt.plot(xx, yy)
plt.grid()
plt.show()
