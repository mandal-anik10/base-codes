'''
PLOTTING OF THE DIFFERENTIAL EQUATION OF A DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS :

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0
y = 1
r = 1
e = 0

w = 100*np.pi
g = 2
w1 = (w-(g**2)/4)**0.5

xx = []
yy = []

n = 500000
xs = 1e-5
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = r*np.exp(-0.5*g*x)*(-0.5*g*np.cos(w1*x+e)-w1*np.sin(w1*x+e))            # slope is being derived analytically

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE DIFFERENTIAL EQUATION OF A DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS")
plt.title("Damping constant 'g' :"+str(g)+"  And Actual angular frequency 'w' :"+str(w))
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["$y''  = -w^2y -gy'$\n$g<2w$"], loc="upper right")
plt.grid()

plt.show()
