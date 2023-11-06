
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 0

h = 0.1
n = 40
x1 = x0
y1 = y0

xx = [x0]
yy = [y0]
zz = [0]
xr = [x0]
yr = [y0]


def m(x, y):
    s = (2*x-2*x**3)*np.exp(-x**2)
    return s


for i in range(n):
    y1 = y1 + h*m(x1, y1)
    x1 = x1 + h
    xx.append(x1)
    yy.append(y1)
    z = (x1**2)*np.exp(-x1**2)
    zz.append(z)

x1 = x0
y1 = y0
yd = y0

for i in range(n):
    m1 = m(x1, yd)
    yd = yd + h*m1
    x1 = x1 + h
    m2 = m(x1, yd)

    y1 = y1 + h*(m1 + m2)/2

    xr.append(x1)
    yr.append(y1)

plt.plot(xx, zz, '-+r')
plt.plot(xx, yy, 'c')
plt.plot(xr, yr, 'b')
plt.legend(['Actual curve', 'Euler Method', 'RK-2 Method'])
plt.grid()
plt.show()
