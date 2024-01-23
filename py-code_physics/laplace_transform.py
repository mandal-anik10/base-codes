'''
Laplace Transform:

Author : Anik Mandal
'''
import numpy as np
import matplotlib.pyplot as plt

(xi, xf, n) = (0, 1, 500)
x = np.linspace(xi, xf, n)
f = np.sinh(2*x)

kk = x
gg = []
for i in range(len(kk)):
    y = f * np.exp(-kk[i] * x)
    g = np.trapz(y, x, dx=x[1]-x[0])
    gg.append(g)

plt.plot(kk, gg, 'r')
plt.xlabel('k')
plt.ylabel('g(k)')
plt.grid()
plt.show()
