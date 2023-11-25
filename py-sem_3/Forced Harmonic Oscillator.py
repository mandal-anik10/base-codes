
# PLOTTING OF THE DIFFERENTIAL EQUATION OF A FORCED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS :


import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0
y = 0
a = 1
b = 1

r = 1
e = np.pi
w = 5*np.pi

xx = []
yy = []

n = 1000000
xs = 0.00001
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = -a*r*w*(np.sin(w*x-e)) + b*100*np.cos(x)/(w**2-1)

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE DIFFERENTIAL EQUATION OF A FORCED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS")
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["$d^2y/dx^2  = -w^2y + f(x)$\n$f(x)=100sin(x)$"], loc="upper right")
plt.grid()

plt.show()
