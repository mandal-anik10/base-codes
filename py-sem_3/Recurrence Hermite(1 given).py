# Recurrence Hermite(1 Function Given):

import matplotlib.pyplot as plt
import numpy as np

# h1x = 2*x
# h0x = 1

xx = np.linspace(0, 2, 1000)
h = 0.00000001

h1x = []
h2x = []


def f(x):
    y = 2 * x
    return y


for i in range(len(xx)):
    h1 = 2 * xx[i]

    df = (f(h1 + h) - f(h1)) / h
    h2 = 2 * xx[i] * h1 - df

    h1x.append(h1)
    h2x.append(h2)

plt.plot(xx, h1x, 'g', xx, h2x, 'r')
plt.legend(['$Hermite Polynomial$ of Degree 1(given)', '$Hermite Polynomial$ of Degree 2(Determined)'])
plt.grid()
plt.show()
