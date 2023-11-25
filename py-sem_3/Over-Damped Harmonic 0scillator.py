
# PLOTTING OF THE DIFFERENTIAL EQUATION OF A OVER-DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS :


import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0
y = 1
a = -1
b = 2

w = np.pi
g = 2.5*w

k1 = -0.5*g-(0.25*g**2-w**2)**0.5
k2 = -0.5*g+(0.25*g**2-w**2)**0.5

xx = []
yy = []

n = 500000
xs = 0.00001
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = k1*a*np.exp(k1*x)+k2*b*np.exp(k2*x)

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE DIFFERENTIAL EQUATION OF A OVER-DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS")
plt.title("Damping constant 'g' :"+str(g)+"  And Actual angular frequency 'w' :"+str(w))
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["$y''  = -w^2y -gy'$"], loc="upper right")
plt.grid()

plt.show()
