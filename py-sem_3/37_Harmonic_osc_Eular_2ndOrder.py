'''
PLOTTING OF THE DIFFERENTIAL EQUATION OF A HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS :

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0.0
y = 0.0

r = 1
g = np.pi
w = 10*np.pi

xx = []
yy = []

n = 500000
xs = 1e-5
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = r*w*(np.cos(w*x+g))         # slope is being derived analytically

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE DIFFERENTIAL EQUATION OF A HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS")
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend([r"$\frac{d^2y}{dx^2}  = -w^2y$"], loc="upper right")
plt.grid()

plt.show()
