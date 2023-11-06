# Laplace Transform:

import numpy as np
from LocalModule.Basic import *
import matplotlib.pyplot as plt

(xi, xf, n) = (0, 1, 500)
x = np.linspace(xi, xf, n)
f = np.sinh(2*x)

kk = x
gg = []
for i in range(len(kk)):
    y = f * np.exp(-kk[i] * x)
    g = Integrate(y, xi, xf, n)
    gg.append(g)

plt.plot(kk, gg, 'r')
plt.grid()
plt.show()
