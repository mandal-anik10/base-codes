'''
Inverse Fourier Transform of a function g(k) to f(x)

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

# function
ki = -10
kf = 10
kn = 500
kk = np.linspace(ki, kf, kn)
aa = kk * np.pi / 2
gg = ((0.5 * np.pi ** 3) ** 0.5) * ((np.sin(aa)) ** 2) / aa ** 2
plt.plot(kk, gg, 'c')

# transformed function
xi = -5
xf = 5
n = 1000
xx = np.linspace(xi, xf, n)
yy = []

for i in range(len(xx)):
    fi = gg * np.cos(xx[i] * kk)
    y = np.trapz(fi, kk, dx=kk[1]-kk[0]) / (2 * np.pi) ** 0.5
    yy.append(y)

plt.plot(xx, yy, 'r')
plt.title("Inverse Fourier Transform of a function")
plt.legend(["k-Space(Actual function)", "x-Space(Function after inverse transform)"])
plt.xlabel("k , x")
plt.ylabel("g(k) , f(x)")
plt.grid()
plt.show()
