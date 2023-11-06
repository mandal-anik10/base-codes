# DETERMINATION OF THE FOURIER SERIES COEFFICIENTS FOR GIVEN SITUATION AND BOUNDARY CONDITIONS :
# AND PLOTTING OF THE EXACT FOURIER FUNCTION FOR DIFFERENT VALUES OF x :

import matplotlib.pyplot as plt
import numpy as np
from Integration import *

print("\n\tDETERMINATION OF THE FOURIER SERIES COEFFICIENTS FOR GIVEN SITUATION AND BOUNDARY CONDITIONS :\n")

xi = -1
xf = 1

xm = -1 / 2

n = 5000
n1 = int(n * abs((xm - xi) / (xf - xi)))
n2 = int(n * abs((xf - xm) / (xf - xi)))
nc = 100

xx = np.linspace(xi, xf, n)
xx1 = np.linspace(xi, xm, n1)
xx2 = np.linspace(xm, xf, n2)

cc = []
cs = []
yy = []

for i in range(nc):
    yc1 = -np.cos(np.pi * i * xx1)
    yc2 = np.cos(np.pi * i * xx2)

    ys1 = -np.sin(np.pi * i * xx1)
    ys2 = np.sin(np.pi * i * xx2)

    sc = Integrate(yc1, xi, xm, n1) + Integrate(yc2, xm, xf, n2)
    ss = Integrate(ys1, xi, xm, n1) + Integrate(ys2, xm, xf, n2)

    cc.append(sc)
    cs.append(ss)

cc[0] = cc[0] / 2
yy = []
zz = np.zeros(n)

print("Coefficients of cosine function : ", cc, "\nCoefficients of sine function : ", cs)

for i in range(n):
    s = 0

    for j in range(nc):
        s = s + cc[j] * np.cos(np.pi * j * xx[i]) + cs[j] * np.sin(np.pi * j * xx[i])

    yy.append(s)

    if xx[i] <= -1 / 2:
        zz[i] = -1
    else:
        zz[i] = 1

plt.plot(xx, yy, '-r', xx, zz, '-.b')

plt.title("FOURIER ANALYSIS OF A FUNCTION" + "\nNumber of points :" + str(n) + " Number of coefficients :" + str(nc))
plt.xlabel("x Data --->")
plt.ylabel("y Data --->")
plt.legend(["Fourier function", "Actual function"])

n = 125
avy = 0
for i in range(len(xx)):
    if -0.5 <= xx[i] <= -0.45:
        avy = avy + yy[i]

plt.grid()

plt.show()
